class Instance:

    def __init__(self, sid, src_sentence, src_sentence_pp, src_tokens, src_embedding):
        self._sid = sid
        self._src_sentence = src_sentence
        self._src_sentence_pp = src_sentence_pp
        self._src_embedding = src_embedding
        self._src_tokens = src_tokens
        self._mt_sentences = {}
        self._mt_sentences_pp = {}
        self._mt_tokens = {}
        self._mt_embeddings = {}
        self._mt_prism_scores = {}

    @property
    def sid(self):
        return self._sid

    @property
    def src_sentence(self):
        return self._src_sentence

    @property
    def src_sentence_pp(self):
        return self._src_sentence_pp

    @property
    def src_tokens(self):
        return self._src_tokens

    @property
    def src_embedding(self):
        return self._src_embedding

    @property
    def mt_sentences(self):
        return self._mt_sentences

    @property
    def mt_sentences_pp(self):
        return self._mt_sentences_pp

    @property
    def mt_tokens(self):
        return self._mt_tokens

    @property
    def mt_embeddings(self):
        return self._mt_embeddings

    @property
    def mt_prism_scores(self):
        return self._mt_prism_scores


    def add_mt(self, system_name, mt_sentence, mt_sentence_pp, mt_tokens, mt_embedding, mt_prism_score):
        self._mt_sentences.update({system_name : mt_sentence})
        self._mt_sentences_pp.update({system_name : mt_sentence_pp})
        self._mt_tokens.update({system_name : mt_tokens})
        self._mt_embeddings.update({system_name : mt_embedding})
        self._mt_prism_scores.update({system_name : mt_prism_score})


    def __str__(self):
        return str(self._sid) + " | " + self._src_sentence