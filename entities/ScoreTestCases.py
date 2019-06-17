import pickle

class ScoreTestCases():
    def __init__(self, num_circuits, num_test_circuits, initial_test_case, max_num_test_cases):
        self._num_circuits = num_circuits
        self._num_test_circuits = num_test_circuits

        self._actual_test_case = initial_test_case - 1
        self._initial_test_case = initial_test_case - 1

        self._max_num_test_cases = max_num_test_cases
        self._best_weights = [[0 for i in range(0, self._num_circuits + self._num_test_circuits)]
                              for i in range(self._max_num_test_cases)]


    def add_test_case(self, circuits, weights):
        for i in range(0, len(circuits)):
            self._best_weights[self._actual_test_case][circuits[i] - 1] = weights[i]

        self._actual_test_case += 1

    def update_weight_test_circuit(self, num_test_case, index_test_circuit, weight):
        self._best_weights[num_test_case - 1][self._num_circuits + index_test_circuit] = weight

    def print_score(self):
        result = '             |'
        for i in range(self._num_circuits):
            result += '           Circuit {0}|'.format(str(i+1))

        for i in range(self._num_test_circuits):
            result += '      Test Circuit {0}|'.format(str(i+1))

        result += '\n' + ('-' * 246) + '\n'
        for i in range(self._initial_test_case, self._actual_test_case):
            result += 'Test case {:3}|'.format(str(i + 1))
            for j in range(len(self._best_weights[i])):
                weight_info = '{:20.4f}'.format(self._best_weights[i][j])
                result += weight_info
                result += '|'

            result += '\n' + ('-' * 246) + '\n'

        print(result)

    def saveScoreInFile(self):
        contentFile = '             |'

        for i in range(self._num_circuits):
            contentFile += '           Circuit {0}|'.format(str(i+1))

        for i in range(self._num_test_circuits):
            contentFile += '      Test Circuit {0}|'.format(str(i+1))

        contentFile += '\n' + ('-' * 246) + '\n'

        contentFile += 'Test case {:3}|'.format(str(self._actual_test_case))

        index_case = self._actual_test_case - 1
        for j in range(len(self._best_weights[index_case])):
            weight_info = '{:20.4f}'.format(self._best_weights[index_case][j])
            contentFile += weight_info
            contentFile += '|'

        filepath = '../TestCasesMetrics/testcase{0}.txt'.format(self._actual_test_case)
        f = open(filepath, 'w+')
        f.write(contentFile)
        f.close()

