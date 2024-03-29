import numpy as np

from Expert import *


class TaskModel(Expert):

    def __init__(self, model_name, predictions, human_scores, bleu_scores, comet_scores, num_models, reward_function):
        self._model_name = model_name
        self._model_predictions = predictions
        self._model_human_scores = human_scores
        self._model_bleu_scores = bleu_scores
        self._model_comet_scores = comet_scores
        super().__init__(model_name, num_models, reward_function)


    @property
    def model_name(self):
        return self._model_name


    def get_human_score(self, s_id):
        return self._model_human_scores[s_id]

    def get_bleu_score(self, s_id):
        return self._model_bleu_scores[s_id]

    def get_comet_score(self, s_id):
        return self._model_comet_scores[s_id]

    def get_model_prediction(self, s_id):
        return self._model_predictions[s_id]


    def output(self, instance_id):

        # handling when models did not translate src
        try:
            prediction = self.get_model_prediction(instance_id)
        except:
            return ""
        else:
            return prediction


    def reward(self, instance_id):

        try: # handling when models did not translate src

            if str.startswith(self._reward_function, "human"):
                reward_value = self.get_human_score(instance_id)

                if np.isnan(reward_value):
                    if self._reward_function == "human": #human-zero
                        reward_value = 0
                    elif self._reward_function == "human-avg":
                        reward_value = self.avg_reward
                    elif self._reward_function == "human-comet":
                        reward_value = self.get_comet_score(instance_id)
                else:
                    reward_value = reward_value * 0.01

            elif self._reward_function == "bleu":
                reward_value = self.get_bleu_score(instance_id)
                reward_value = reward_value * 0.01

            elif self._reward_function == "comet":
                reward_value = self.get_comet_score(instance_id)

            else:
                return # FIXME throw exception
        except:
            return 0
        else:
            return reward_value


    def __str__(self):
        return self._model_name + " | Current weight: " + str(self.weight_as_probability)



