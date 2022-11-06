from tqdm import tqdm

from io_utils import *
from nlp_utils import *


def src_to_embeddings(task, lang, corpus_path, embedder):
    
    if lang == "en-de" and task == "WMT19":
        idx = 'sent_id'
    else:
        idx = 'sid'

    emb_src = {}

    corpus_df = load_dataframe_from_pickle(corpus_path)

    src_ids = corpus_df[[idx, 'src']]

    for s_id in tqdm(corpus_df[idx]):
        if s_id not in emb_src.keys():
            src = src_ids.loc[src_ids[idx] == s_id].src.iloc[0]
            #print(src)
            src_pp = remove_punctuation(src)
            src_embedding = embedder.encode([src_pp])
            emb_src.update({s_id : src_embedding})

    return emb_src

    
def mt_to_embeddings(task, lang, corpus_path, embedder):

    if lang == "en-de" and task == "WMT19":
        idx = 'sent_id'
    else:
        idx = 'sid'

    emb_mt = {}

    corpus_df = load_dataframe_from_pickle(corpus_path)

    all_model_names = list(corpus_df.system.unique())

    for model_name in tqdm(all_model_names):

        system_df = corpus_df.loc[corpus_df['system'] == model_name]

        sub_emb_mt = {}

        for s_id in system_df[idx]:

            current_id_df = system_df.loc[system_df[idx] == s_id]

            mt = current_id_df['mt'].iloc[0]
            #print(mt)

            mt_pp = remove_punctuation(mt)
            mt_embedding = embedder.encode([mt_pp])

            sub_emb_mt.update({s_id: mt_embedding})

            emb_mt.update({model_name: sub_emb_mt})

    return emb_mt
