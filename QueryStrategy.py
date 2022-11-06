import random
import numpy as np
import sacrebleu
from nltk import FreqDist
from nltk.util import everygrams

from nlp_utils import *
from Expert import *


class QueryStrategy(Expert):

    def __init__(self, strategy_name, similarity_measure=None, threshold=0.5, num_qs=None, reward_function=None):
        self._sm = similarity_measure
        self._threshold = threshold
        self._last_vote = None
        super().__init__(strategy_name, num_qs, reward_function)
        
    @property
    def sm(self):
        return self._sm

    def output(self, params):
        
        instance_to_query, l, u = params        
        self._last_vote = self.vote_instance(instance_to_query, labeled_so_far=l, unlabeled_so_far=u)

        print("{} vote: {}".format(self.name, self._last_vote))
        
        return self._last_vote


    def reward(self, params): # NOTE: only called if there was an update on the inner OL (i.e., when forecaster's vote was True)

        # for EWAF, regret is based on cumulative loss; for EXP3, regret is based on avg loss:
        previous_regret, current_regret, mt_algorithm = params

        regret_var = current_regret - previous_regret


        if mt_algorithm == "EWAF":
            if self._last_vote: # voted for update
                reward_value = 1 - regret_var # higher reward when no regret
            else: # voted against update
                reward_value = regret_var # higher reward when maximum regret
        else:
            if self._last_vote:
                reward_value = 1 - (regret_var + 1) / 2
            else:
                reward_value = (regret_var + 1) / 2
        
        print("regret: {} - {} = {}; reward: {}".format(current_regret, previous_regret, regret_var, reward_value))

        return reward_value


    def vote_instance(self, instance_to_query, labeled_so_far=None, unlabeled_so_far=None):
        pass


    """
    for query strategies that use similarity
    
    """
    def apply_similarity_measure(self, s1_str, s2_str, s1_tok, s2_tok, s1_emb, s2_emb):
        if self._sm == "jac":
            return jaccard_similarity(s1_tok, s2_tok)

        if self._sm == "dice":

            return dice_similarity(s1_tok, s2_tok)

        if self._sm == "BERT":
            return cosine_similarity(s1_emb, s2_emb)

        if self._sm == "BLEU":
            bleu_sim = sacrebleu.corpus_bleu([s1_str], [[s2_str]])
            return (bleu_sim.score / 100.0)


################################################################################

class RandomSampling(QueryStrategy):

    def __init__(self, seed, num_qs=None, reward_function=None):
        random.seed(seed)
        super().__init__("Random", similarity_measure=None, threshold=None, num_qs=num_qs, reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None, unlabeled_so_far=None):

        return bool(random.getrandbits(1))


    def __str__(self):
        return "Random"


################################################################################

class Diversity(QueryStrategy):
    
    def __init__(self, similarity_measure=None, threshold=0.5, num_qs=None, reward_function=None):
        super().__init__("Diversity", similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None, unlabeled_so_far=None):

        sim_list = [self.apply_similarity_measure(instance_to_query.src_sentence_pp, l.src_sentence_pp, instance_to_query.src_tokens, l.src_tokens, instance_to_query.src_embedding, l.src_embedding) for l in labeled_so_far]
        avg_similarity = np.mean(sim_list)
        
        print("{} - avg sim: {}".format(self, avg_similarity))

        if avg_similarity < self._threshold:
            return True
        return False


    def __str__(self):
        return "Diversity | sim_measure={} | threshold={}".format(self._sm, self._threshold)


################################################################################

class Density(QueryStrategy):
    
    def __init__(self, similarity_measure=None, threshold=0.5, num_qs=None, reward_function=None):
        super().__init__("Density", similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None, unlabeled_so_far=None):

        sim_list = [self.apply_similarity_measure(instance_to_query.src_sentence_pp, u.src_sentence_pp, instance_to_query.src_tokens, u.src_tokens, instance_to_query.src_embedding, u.src_embedding) for u in unlabeled_so_far]
        #print(sim_list)
        avg_similarity = np.mean(sim_list)
        
        print("{} - avg sim: {}".format(self, avg_similarity))

        if avg_similarity > self._threshold:
            return True
        return False


    def __str__(self):
        return "Density | sim_measure={} | threshold={}".format(self._sm, self._threshold)

################################################################################

class NGramDiversity(QueryStrategy):

    def __init__(self, max_n=3, threshold=0.5, num_qs=None, reward_function=None):

        self._max_n = max_n
        super().__init__("N-gram Diversity",
                         threshold=threshold, num_qs=num_qs,
                         reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None,
                      unlabeled_so_far=None):

        L_ngrams = get_ngrams_from_instances(labeled_so_far, max_len=self._max_n)

        sentence_ngrams = list(everygrams(instance_to_query.src_tokens, max_len=self._max_n))

        diversity = np.sum([int(ngram not in L_ngrams) for ngram in sentence_ngrams]) / len(sentence_ngrams)

        print("{} - ngram diversity: {}".format(self, diversity))

        if diversity > self._threshold:
            return True
        return False


    def __str__(self):
        return "N-gram Diversity | threshold={}".format(self._threshold)

################################################################################


class NGramDensity(QueryStrategy):

    def __init__(self, lmbd=1, max_n=3, threshold=0.5, num_qs=None, reward_function=None):

        self._lambda = lmbd
        self._max_n = max_n
        super().__init__("N-gram Density",
                         threshold=threshold, num_qs=num_qs,
                         reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None,
                      unlabeled_so_far=None):

        L_ngrams = get_ngrams_from_instances(labeled_so_far, max_len=self._max_n)
        U_ngrams = get_ngrams_from_instances(unlabeled_so_far, max_len=self._max_n)

        L_counts = FreqDist()
        U_counts = FreqDist()

        L_counts.update(L_ngrams)
        U_counts.update(U_ngrams)

        sentence_ngrams = list(everygrams(instance_to_query.src_tokens, max_len=self._max_n))

        density = np.sum(
            [U_counts[ngram] * np.exp(-self._lambda * L_counts[ngram]) for ngram
             in sentence_ngrams]) / (len(sentence_ngrams) * len(U_ngrams))

        print("{} - ngram density: {}".format(self, density))

        if density > self._threshold:
            return True
        return False


    def __str__(self):
        return "N-gram Density | threshold={}".format(self._threshold)

################################################################################

# aka Translation Disagreement
class QueryByCommittee(QueryStrategy):
    
    def __init__(self, similarity_measure=None, threshold=0.5, num_qs=None, reward_function=None):
        super().__init__("Query-by-committee", similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None, unlabeled_so_far=None):

        avg_agreement = 0

        mt_sentences_list = list(instance_to_query.mt_sentences.values())
        mt_tokens_list = list(instance_to_query.mt_tokens.values())
        mt_embeddings_list = list(instance_to_query.mt_embeddings.values())

        mt_length = len(mt_sentences_list)

        n_combos = (np.square(mt_length) - mt_length) / 2

        for i in range(mt_length):
            for j in range(i):
                 avg_agreement = avg_agreement + self.apply_similarity_measure(mt_sentences_list[i], mt_sentences_list[j], mt_tokens_list[i], mt_tokens_list[j], mt_embeddings_list[i], mt_embeddings_list[j])

        avg_agreement = avg_agreement / n_combos
        
        print("{} - avg sim: {}".format(self, avg_agreement))

        if avg_agreement < self._threshold:
            return True
        return False


    def __str__(self):
        return "Query By Committee | sim_measure={} | threshold={}".format(self._sm, self._threshold)


################################################################################

# aka Translation Difficulty
class QualityEstimation(QueryStrategy):

    def __init__(self, similarity_measure=None, threshold=-5, num_qs=None, reward_function=None):
        super().__init__("Quality Estimation",
                         similarity_measure=similarity_measure,
                         threshold=threshold, num_qs=num_qs,
                         reward_function=reward_function)


    def vote_instance(self, instance_to_query, labeled_so_far=None,
                      unlabeled_so_far=None):

        avg_quality = 0

        mt_prism_scores = list(instance_to_query.mt_prism_scores.values())
        avg_quality = np.mean(mt_prism_scores)

        print("{} - avg sim: {}".format(self, avg_quality))

        if avg_quality < self._threshold:
            return True
        return False


    def __str__(self):
        return "Quality Estimation | sim_measure={} | threshold={}".format(
            self._sm, self._threshold)


################################################################################

def init_query_strategy(strategy_name, params, num_qs, reward_function, seed=0):

    if strategy_name == "random":
        query_strategy = RandomSampling(seed, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "Div":
        similarity_measure, threshold = params
        
        query_strategy = Diversity(similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "Den":
        similarity_measure, threshold = params
        
        query_strategy = Density(similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "DivNg":
        max_ngram, threshold = params

        query_strategy = NGramDiversity(max_n=int(max_ngram), threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "DenNg":
        max_ngram, threshold = params

        query_strategy = NGramDensity(max_n=int(max_ngram), threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "QbC":
        similarity_measure, threshold = params
        
        query_strategy = QueryByCommittee(similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy

    elif strategy_name == "QEst":
        similarity_measure, threshold = params
        
        query_strategy = QualityEstimation(similarity_measure=similarity_measure, threshold=threshold, num_qs=num_qs, reward_function=reward_function)
        return query_strategy
