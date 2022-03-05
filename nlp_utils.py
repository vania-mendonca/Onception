import scipy.spatial
import string

import nltk
from nltk.util import everygrams

################################################################################

def remove_punctuation(sentence):
    return sentence.translate(str.maketrans('', '', string.punctuation))


def get_ngrams_from_instances(instance_list, max_len=3):

    all_n_grams = []
    for inst in instance_list:
        inst_tokens = nltk.word_tokenize(inst.src_sentence_pp.lower())
        inst_ngrams = list(everygrams(inst_tokens, max_len=max_len))
        all_n_grams = all_n_grams + inst_ngrams

    return all_n_grams


################################################################################

"""
Simple overlap between two Python lists
(over the length of list1, assuming both lists have the same length and unique values)
"""

def overlap(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    
#     print(s1)
#     print(s2)
    
#     print(len(s1.intersection(s2)))
#     print(len(s1))
    
    overlap = len(s1.intersection(s2)) / len(s1)
    
    return overlap


"""
Jaccard similarity between two Python lists
"""
def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    
    if len(s1.union(s2)) == 0:
        return 0
    return len(s1.intersection(s2)) / len(s1.union(s2))


"""
Dice similarity between two Python lists
"""
def dice_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    
    total_len = len(s1) + len(s2)
    #print(len(s1))
    #print(len(s2))
    
    if total_len == 0:
        return 0
    return len(s1.intersection(s2)) / total_len


"""
Cosine similarity between two Python vectors (1 - cosine distance)
"""
def cosine_similarity(vec1, vec2):
    return 1 - scipy.spatial.distance.cosine(vec1, vec2)
