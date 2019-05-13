class ScoreTestCases():
    def __init__(self, num_circuits, num_test_circuits):
        self._num_circuits = num_circuits
        self._num_test_circuits = num_test_circuits

        self._best_weights = []

    def add_test_case(self, circuits, weights):

        self._best_weights.append([0 for i in range(0, self._num_circuits + self._num_test_circuits)])

        for i in range(0, len(circuits)):
            index_last_best_weight = len(self._best_weights) - 1
            self._best_weights[index_last_best_weight][circuits[i] - 1] = weights[i]

    def update_weight_test_circuit(self, num_test_case, index_test_circuit, weight):
        self._best_weights[num_test_case - 1][self._num_circuits + index_test_circuit] = weight

    def print_score(self):
        print('HOLA')
        result = '             |'
        for i in range(self._num_circuits):
            result += '           Circuit {0}|'.format(str(i+1))

        for i in range(self._num_test_circuits):
            result += '      Test Circuit {0}|'.format(str(i+1))

        result += '\n' + ('-' * 246) + '\n'
        for i in range(len(self._best_weights)):
            result += 'Test case {:3}|'.format(str(i + 1))
            for j in range(len(self._best_weights[i])):
                weight_info = '{:20.4f}'.format(self._best_weights[i][j])
                result += weight_info
                result += '|'

            result += '\n' + ('-' * 246) + '\n'

        print(result)




