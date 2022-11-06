from pathlib import Path # only supported in Python 3
import os
import sys
import getopt
from nltk.tokenize import word_tokenize
import jieba

from io_utils import *
from nlp_utils import *
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

    # Online learning
    algorithm = "EWAF"  # "EXP3" # "EWAF
    reward_function = "human"
    eta_param = 8  # weight update (EWAF)
    dp = 2  # reward decimal places
    # "human"
    # "human-avg" "human-comet" "comet" "bleu" # (only when using DA scores)


    # MT params
    src_lang = "en"
    mt_lang = "de"
    task = "WMT19"  # "WMT20_pSQM" # "WMT19"

    # Setup
    seed = 0

    ###
    # Getting params from command line:

    try:
        opts, args = getopt.getopt(argv, "", ["qs=", "sm=", "ts=", "alg=", "rw=", "task=", "src=", "mt=", "run="])

    except getopt.GetoptError:
        print("troll_al.py --qs=<query_strategy> --sm=<similarity_measure> "
              "--ts=<threshold> --alg=<online_algorithm> --rw=<reward_func> "
              "--task=<task> --src=<src_lang> --mt=<mt_lang> --run=<num_no>")
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

        if opt == '--task':
            task = arg
        if opt == '--src':
            src_lang = arg
        if opt == '--mt':
            mt_lang = arg

        if opt == '--run':
            seed = int(arg)


    ##

    # depending on args:

    run = str(seed)
    lang = src_lang + "-" + mt_lang

    ################

    data_folder = Path("datasets/{}/{}/".format(task, lang))
    emb_folder = Path("embeddings/{}/".format(task))
    results_folder = Path("results/{}/{}/run{}/".format(task, lang, run))

    if not os.path.isdir(results_folder.as_posix()):
        os.makedirs(results_folder.as_posix())


    ################
    # Loading corpus

    print("Loading corpus...")

    learn_sent_ids_filepath = data_folder / "shuf_ids_{}.txt".format(run)
    learning_ids = load_int_list_from_txt(learn_sent_ids_filepath)
    print("First:", learning_ids[0])

    corpus_filepath = data_folder / "{}_prism.pickle".format(lang)
    full_corpus = load_dataframe_from_pickle(corpus_filepath)

    full_corpus['src'] = full_corpus['src'].astype('string')
    full_corpus['mt'] = full_corpus['mt'].astype('string')

    ################
    # Loading embeddings

    if sim_measure == "BERT":
        print("Loading embeddings...")

        src_emb_filepath = emb_folder / "BERT_{}_src_{}.pickle".format(lang, src_lang)
        mt_emb_filepath = emb_folder / "BERT_{}_mt_{}.pickle".format(lang, mt_lang)

        src_embeddings = load_dict_from_pickle(src_emb_filepath)
        mt_embeddings = load_dict_from_pickle(mt_emb_filepath)


    ################
    # Loading MT data

    print("Loading MT data...")

    idx = 'sid'

    if task == "WMT19" and lang == "en-de":
        idx = 'sent_id'

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

    query_strategy = init_query_strategy(AL_strategy, (sim_measure, threshold), 1, None, seed=seed)
    print(query_strategy)

    ###
    print("Generating AL instances...")

    L = []
    U = []

    for sent_id in learning_ids:

        print("sid:", sent_id)

        full_info = full_corpus.loc[full_corpus[idx] == sent_id]

        src_sentence = str(full_info['src'].iloc[0])
        src_sentence_pp = remove_punctuation(src_sentence)

        if src_lang == "zh":
            src_tokens = jieba.lcut(src_sentence_pp.lower())
        else:
            src_tokens = word_tokenize(src_sentence_pp.lower())

        if sim_measure == "BERT":  # keep this for efficiency
            src_embedding = src_embeddings[sent_id]
        else:
            src_embedding = None

        inst = Instance(sent_id, src_sentence, src_sentence_pp, src_tokens, src_embedding)

        model_names = list(full_info.system.unique())

        for model_name in model_names:
            system_info = full_info.loc[full_corpus['system'] == model_name]

            mt_sentence = str(system_info['mt'].iloc[0])
            mt_sentence_pp = remove_punctuation(mt_sentence)

            if mt_lang == "zh":  # not gonna happen for now
                mt_tokens = jieba.lcut(mt_sentence_pp.lower())
            else:
                mt_tokens = word_tokenize(mt_sentence_pp.lower())

            if sim_measure == "BERT":  # keep this for efficiency
                mt_embedding = mt_embeddings[model_name][sent_id]
            else:
                mt_embedding = None

            mt_prism_score = system_info['prism_score'].iloc[0]

            inst.add_mt(model_name, mt_sentence, mt_sentence_pp, mt_tokens, mt_embedding, mt_prism_score)

        U.append(inst)

    print(len(U))


    ################
    # OL init

    print("Init Online algorithm...")

    oa = init_online_algorithm(algorithm, num_of_models, decimal_places=dp,
                               eta_value=eta_param,
                               reward_function=reward_function, seed=seed)
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


        t = t + 1

    print("Done.")



################################################################################

if __name__ == "__main__":
   main(sys.argv[1:])