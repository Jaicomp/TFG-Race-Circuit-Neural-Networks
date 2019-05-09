class ScoreTestCases():
    def __init__(self, num_circuits, num_test_circuits):
        self._num_circuits = num_circuits
        self._num_test_circuits = num_test_circuits
        self._num_test_cases = (2 ** self._num_circuits) - 1

        self._best_weights = []
        self._num_test_cases = 0

    def add_test_case(self, circuits, weights):

        self._best_weights[self._num_test_cases] = [0 for i in range(0, self._num_circuits + self._num_test_circuits)]

        for i in range(0, self._num_circuits):
            self._best_weights[self._num_test_cases][circuits[i] - 1] = weights[i]

        self._num_test_cases += 1

    def update_weight_test_circuit(self, num_test_case, num_test_circuit, weight):
        self._best_weights[num_test_case][num_test_circuit] = weight


    def print_score(self):
        pass






