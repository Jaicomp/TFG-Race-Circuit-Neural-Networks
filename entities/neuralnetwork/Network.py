import numpy


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [numpy.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [numpy.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]

    @staticmethod
    def sigmoid(z):
        return 1.0 / (1.0 + numpy.exp(-z))

    def softmax(z):
        return numpy.exp(z) / (sum(numpy.exp(z)))

    def tanh(z):
        return numpy.tanh(z)
    def arctan(z):
        return numpy.arctan(z)


    def tangenteHiperbolica(z):
        return (numpy.exp(z) - numpy.exp(-z)) / (numpy.exp(z) + numpy.exp(-z))

    def gaussian(x,c):
        return c*numpy.exp(-numpy.power(x, 2.0))


    def feedforward(self, a):
        """Return the output of the network if "a" is input."""
        for b, w in zip(self.biases, self.weights):
            a = Network.sigmoid(numpy.dot(w, a)+b)

        return a

    def apply_noise(self):
        self.biases = [x + numpy.random.uniform(-0.1, 0.1) for x in self.biases]
        self.weights = [x + numpy.random.uniform(-0.1, 0.1) for x in self.weights]

    def copy(self):
        n = Network(self.sizes)
        n.biases = self.biases.copy()
        n.weights = self.weights.copy()
        return n


