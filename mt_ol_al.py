from pathlib import Path # only supported in Python 3
import sys
import getopt

from io_utils import *
from OnlineAlgorithm import *
from QueryStrategy import *
from TaskModel import *
from Instance import *

################################################################################

def main(argv):

    #### PARAMS ####

    ###
    # Default param values:

    # AL
    AL_strategy = "Div"
    sim_measure = "jac"
    threshold = 0.5

    # EWAF / EXP3 params
    algorithm = "EWAF"  # "EXP3" # "EWAF
    reward_function = "human"
    # "human" "human-avg" "human-comet" "comet" "bleu"

    # MT params
    src_lang = "en"
    mt_lang = "de"

    # Setup
    run = "1"

    ###
    # Getting params from command line:

    try:
        opts, args = getopt.getopt(argv, "", ["qs=", "sm=", "ts=", "alg=", "rw=", "src=", "mt=", "run="])

    except getopt.GetoptError:
        print("troll_al.py --qs=<query_strategy> --sm=<similarity_measure> "
              "--ts=<threshold> --alg=<online_algorithm> --rw=<reward_func> "
              "--src=<src_lang> --mt=<mt_lang> --run=<num_no>")
        sys.exit(2)

    for opt, arg in opts:

        print(opt, arg)

        if opt == '--qs':
            AL_strategy = arg
        if opt == '--sm':
            sim_measure = arg
        if opt == '--ts':
            threshold = float(arg)

        if opt == '--alg':
            algorithm = arg
        if opt == '--rw':
            reward_function = arg

        if opt == '--src':
            src_lang = arg
        if opt == '--mt':
            mt_lang = arg

        if opt == '--run':
            run = arg

    ###

    # Online learning
    eta_param = 8  # weight update (EWAF)
    dp = 2  # reward decimal places

    # MT
    lang = src_lang + "-" + mt_lang


    ################

    data_folder = Path("datasets/{}/".format(lang))
    emb_folder = Path("embeddings/")
    results_folder = Path("results/{}/".format(lang))


    ################
    # Loading corpus

    print("Loading corpus...")

    learn_sent_ids_filepath = data_folder / "shuf_ids.txt"
    #corpus_filepath = data_folder / "{}.pickle".format(lang)
    corpus_filepath = data_folder / "{}_prism.pickle".format(lang)

    learning_ids = load_int_list_from_txt(learn_sent_ids_filepath)
    print("First:", learning_ids[0])

    full_corpus = load_dataframe_from_pickle(corpus_filepath)


    ################
    # Loading embeddings

    print("Loading embeddings...")

    src_emb_filepath = emb_folder / "BERT_{}_src_{}.pickle".format(lang, src_lang)
    mt_emb_filepath = emb_folder / "BERT_{}_mt_{}.pickle".format(lang, mt_lang)

    src_embeddings = load_dict_from_pickle(src_emb_filepath)
    mt_embeddings = load_dict_from_pickle(mt_emb_filepath)


    ################
    # Loading MT data

    print("Loading MT data...")

    if lang == "en-de":
        idx = 'sent_id'
    else:
        idx = 'sid'

    all_model_names = list(full_corpus.system.unique())
    all_models = []

    num_of_models = len(all_model_names)

    for model_name in all_model_names:
        system_info = full_corpus.loc[full_corpus['system'] == model_name]

        translations = dict(zip(system_info[idx], system_info['mt']))
        human_scores = dict(zip(system_info[idx], system_info['raw_score']))
        bleu_scores = dict(zip(system_info[idx], system_info['bleu_score']))
        comet_scores = dict(zip(system_info[idx], system_info['comet_score']))

        model = TaskModel(model_name, translations, human_scores, bleu_scores,
                          comet_scores, num_of_models, reward_function)
        all_models.append(model)

        print(model)


    ################
    # AL init

    print("Init AL query strategy...")

    query_strategy = init_query_strategy(AL_strategy, (sim_measure, threshold), 1, None)
    print(query_strategy)

    ###
    print("Generating AL instances...")

    L = []
    U = []

    for sent_id in learning_ids:

        full_info = full_corpus.loc[full_corpus[idx] == sent_id]

        src_sentence = str(full_info['src'].iloc[0])
        src_sentence_pp = remove_punctuation(src_sentence)
        src_embedding = src_embeddings[sent_id]

        inst = Instance(sent_id, src_sentence, src_sentence_pp, src_embedding)

        model_names = list(full_info.system.unique())

        for model_name in model_names:
            system_info = full_info.loc[full_corpus['system'] == model_name]

            mt_sentence = str(system_info['mt'].iloc[0])
            mt_sentence_pp = remove_punctuation(mt_sentence)
            mt_embedding = mt_embeddings[model_name][sent_id]
            mt_prism_score = float(system_info['prism_score'].iloc[0])

            inst.add_mt(model_name, mt_sentence, mt_sentence_pp, mt_embedding, mt_prism_score)

        U.append(inst)

    print(len(U))


    ################
    # OL init

    print("Init Online algorithm...")

    oa = init_online_algorithm(algorithm, num_of_models, decimal_places=dp,
                               eta_value=eta_param,
                               reward_function=reward_function)
    print(oa)

    ###
    print("Init output files...")

    weights_filepath = results_folder / "weights_{}_{}_{}_{}_{}_{}_{}_{}.csv".format(
        AL_strategy, sim_measure, threshold, algorithm, reward_function, dp, eta_param, run)

    # initial weights
    models_str = [str(m.model_name) for m in all_models]
    weights_str = [str(w) for w in oa.weights_as_probabilities]

    with weights_filepath.open("w", encoding="utf8") as f:
        print(','.join(models_str), file=f)
        print(','.join(weights_str), file=f)

    # regret
    regret_filepath = results_folder / "regret_{}_{}_{}_{}_{}_{}_{}_{}.csv".format(
        AL_strategy, sim_measure, threshold, algorithm, reward_function, dp, eta_param, run)

    with regret_filepath.open("w", encoding="utf8") as f:
        print("{}_{}_{}_{}".format(algorithm, reward_function, dp, eta_param),
              file=f)


    ################
    # OL process

    print("##################### Online learning process #####################")

    t = 1
    U_copy = U.copy()

    for sent_id in learning_ids:

        current_inst = U_copy[t - 1]

        print(" ------------------------- ITERATION {} -------------------------".format(t))

        f_prediction = oa.forecaster(all_models, params=sent_id)

        if t == 1 or query_strategy.vote_instance(current_inst,
                                                  labeled_so_far=L,
                                                  unlabeled_so_far=U):
            oa.update(all_models, t, params=sent_id)
            L.append(current_inst)
            U.remove(current_inst)

            ### print weights
            weights_str = [str(w) for w in oa.weights_as_probabilities]
            with weights_filepath.open("a", encoding="utf8") as f:
                print(','.join(weights_str), file=f)

            ### print regret
            with regret_filepath.open("a", encoding="utf8") as f:
                print(oa.regret, file=f)

        t = t + 1

    print("Done.")



################################################################################

if __name__ == "__main__":
   main(sys.argv[1:])