import numpy as np
import random
from random import choices

class OnlineAlgorithm:
    
    def __init__(self, num_experts, decimal_places, reward_function, seed):
        self._reward_decimal_places = decimal_places
        self._reward_function=reward_function
        self._chosen_expert = None
        self._weights = [1 for i in range(num_experts)]
        self._weights_as_probabilities = [1 / num_experts for i in range(num_experts)]
        self._forecaster_cumulative_loss = 0
        self._optimal_policy_loss = 0
        self._regret = 0
        self._previous_regret = 0
        random.seed(seed)
        
    @property
    def chosen_expert(self):
        return self._chosen_expert
    
    @property
    def weights_as_probabilities(self):
        return self._weights_as_probabilities

    @property
    def regret(self):
        return self._regret

    @property
    def previous_regret(self):
        return self._previous_regret

    
    def forecaster(self, experts, params=None):    
        
#         print(len(experts))
#         print(self._weights_as_probabilities)

        experts_votes = [expert.output(params) for expert in experts]
        self._chosen_expert = choices(range(0, len(experts)), self._weights_as_probabilities)[0]

        return experts_votes[self._chosen_expert]


    def update(self, experts, current_iteration, params=None):
        pass


    def _reward_(self, expert, params=None):

        reward_value = expert.reward(params) # instance_id for MT scenario

        if not(self._reward_decimal_places == None):
            return np.round(reward_value, decimals=self._reward_decimal_places)
        else:
            return reward_value


################################################################################

class EWAF(OnlineAlgorithm):

    def __init__(self, num_experts, decimal_places, eta, reward_function, seed):
        self._eta = eta
        super().__init__(num_experts, decimal_places, reward_function, seed)


    def update(self, experts, current_iteration, params=None):
        num_experts = len(experts)

        self._weights = []
        self._weights_as_probabilities = []

        current_losses = []

        for j in range(len(experts)):

            print(experts[j].name)

            expert_reward = self._reward_(experts[j], params=params)
            expert_loss = 1 - expert_reward

            current_losses.append(expert_loss)

            experts[j].avg_reward = experts[j].cumulative_reward / max(1, (current_iteration - 1))

            experts[j].cumulative_reward = experts[j].cumulative_reward + expert_reward
            experts[j].cumulative_loss = experts[j].cumulative_loss + expert_loss


            if j == self.chosen_expert:
                self._forecaster_cumulative_loss = self._forecaster_cumulative_loss + expert_loss

            ## weight update

            eta = np.sqrt((self._eta * np.log(num_experts)) / current_iteration)
            experts[j].weight = np.exp(- eta * experts[j].cumulative_loss)
            self._weights.append(experts[j].weight)

        ## regret

        self._optimal_policy_loss = self._optimal_policy_loss + min(current_losses)
        
        # debug
        print("Current losses: ", current_losses)
        print("Forecaster total loss - Optimal policy total loss: {} - {}".format(self._forecaster_cumulative_loss, self._optimal_policy_loss))
        
        self._previous_regret = self._regret        
        self._regret = self._forecaster_cumulative_loss - self._optimal_policy_loss

        ## weight update

        total_weight =  np.sum(self._weights)

        for expert in experts:
            expert.weight_as_probability = expert.weight / total_weight
            self._weights_as_probabilities.append(expert.weight_as_probability)


    def __str__(self):
        return "EWAF | decimal places=" + str(self._reward_decimal_places) + " | eta=" + str(self._eta) + " | reward=" + self._reward_function


################################################################################

class EXP3(OnlineAlgorithm):

    def __init__(self, num_arms, decimal_places, reward_function, seed):

        self._arms_use_count = [0 for i in range(num_arms)]
        super().__init__(num_arms, decimal_places, reward_function, seed)


    def update(self, arms, current_iteration, params=None):

        num_arms = len(arms)

        arm_chosen_loss = 0
        arms_avg_loss = [0 for i in range(num_arms)]

        arm_chosen = arms[self._chosen_expert]
        print(arm_chosen.name)

        ## REWARD / LOSS


        for j in range(len(arms)):
            arm_reward = self._reward_(arms[j], params=params)
            arm_reward_hat = arm_reward / arms[j].weight_as_probability
            arm_loss = 1 - arm_reward


            # NOTE: stored for the human-avg fallback score
            arms[j].cumulative_reward = arms[j].cumulative_reward + arm_reward
            arms[j].avg_reward = arms[j].cumulative_reward / max(1, (current_iteration - 1))


            # Actual loss
            if j == self._chosen_expert:
                arm_chosen_loss = arm_loss
                arm_chosen.cumulative_loss = arms[j].cumulative_loss + arm_loss
                arm_chosen.cumulative_loss_hat = arm_chosen.cumulative_loss_hat + (1 - arm_reward_hat)

                self._forecaster_cumulative_loss = self._forecaster_cumulative_loss + arm_loss
                self._arms_use_count[j] = self._arms_use_count[j] + 1


        # Best-worst mean init:
        for j in range(len(arms)):

            if self._arms_use_count[j] == 0:
                arms_avg_loss[j] = np.mean([0, arm_chosen_loss])

            elif j == self._chosen_expert: # always >= 1
                if self._arms_use_count[j] == 1:
                    arms_avg_loss[j] = arm_chosen_loss
                else:
                    arms_avg_loss[j] = arm_chosen.cumulative_loss / self._arms_use_count[j]

        ## REGRET

        forecaster_avg_loss = self._forecaster_cumulative_loss / current_iteration
        optimal_avg_loss = min(arms_avg_loss)
        

        # debug
        print("Forecaster total loss - Optimal policy total loss: {} - {}".format(self._forecaster_cumulative_loss, self._optimal_policy_loss))
        
        self._previous_regret = self._regret

        self._regret = forecaster_avg_loss - optimal_avg_loss


        ## WEIGHT UPDATE

        eta = np.sqrt((2 * np.log(num_arms)) / (current_iteration * num_arms))
        arm_chosen.weight = np.exp(- eta * arm_chosen.cumulative_loss_hat)

        self._weights[self._chosen_expert] = arm_chosen.weight
        total_weight = np.sum(self._weights)

        arm_chosen.weight_as_probability = arm_chosen.weight / total_weight
        self._weights_as_probabilities = [ w / total_weight for w in self._weights]
        
        print("Current weight_p", arm_chosen.weight_as_probability)


    def __str__(self):
        return "EXP3 | decimal places=" + str(self._reward_decimal_places) + " | reward=" + self._reward_function


################################################################################


def init_online_algorithm(algorithm, num_experts, decimal_places=None, eta_value=8,  reward_function="human", seed=0):

    if algorithm == "EWAF":
        return EWAF(num_experts, decimal_places, eta_value, reward_function, seed)
    elif algorithm == "EXP3":
        return EXP3(num_experts, decimal_places, reward_function, seed)
    else:
        return # FIXME throw exception