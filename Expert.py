

class Expert:

    def __init__(self, expert_name, num_experts, reward_function):
        
        self._name = expert_name

        self._reward_function = reward_function

        self._avg_reward = 0
        self._cumulative_reward = 0
        self._cumulative_reward_hat = 0
        self._cumulative_loss = 0
        self._cumulative_loss_hat = 0

        self._weight = 1
        self._weight_as_probability = 1 / num_experts
        self._qvalue = 0

    @property
    def name(self):
        return self._name

    @property
    def avg_reward(self):
        return self._avg_reward

    @avg_reward.setter
    def avg_reward(self, ar):
        self._avg_reward = ar

    @property
    def cumulative_reward(self):
        return self._cumulative_reward

    @cumulative_reward.setter
    def cumulative_reward(self, cr):
        self._cumulative_reward = cr
        
    @property
    def cumulative_reward_hat(self):
        return self._cumulative_reward_hat

    @cumulative_reward_hat.setter
    def cumulative_reward_hat(self, cr):
        self._cumulative_reward_hat = cr

    @property
    def cumulative_loss(self):
        return self._cumulative_loss

    @cumulative_loss.setter
    def cumulative_loss(self, cl):
        self._cumulative_loss = cl
        
    @property
    def cumulative_loss_hat(self):
        return self._cumulative_loss_hat

    @cumulative_loss_hat.setter
    def cumulative_loss_hat(self, cl):
        self._cumulative_loss_hat = cl

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, w):
        self._weight = w

    @property
    def weight_as_probability(self):
        return self._weight_as_probability

    @weight_as_probability.setter
    def weight_as_probability(self, w):
        self._weight_as_probability = w

    @property
    def qvalue(self):
        return self._qvalue

    @qvalue.setter
    def qvalue(self, q):
        self._qvalue = q


    def output(self, params):
        pass

    def reward(self, params):
        pass