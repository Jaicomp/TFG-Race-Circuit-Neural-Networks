import random
import math
# Third-party libraries
import numpy as np
from typing import List

class NetworkAmbSensors(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    def sigmoid_prime(z):
        """Derivative of the sigmoid function."""
        return NetworkAmbSensors.sigmoid(z) * (1 - NetworkAmbSensors.sigmoid(z))




    def tangenteHiperbolica(z):
        #print(np.exp(z) + np.exp(-z))
        #if(np.exp(z) + np.exp(-z))>100000:
        #    v=0
        #else:

        v=(np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))
        v=(1+v)/2
        #print(v)
        return v

    def tangentHiperbolica_prime(z):
        return 1- np.power(NetworkAmbSensors.tangenteHiperbolica(z),2.0)




    def sizes(self):

        return self.sizes
    def biases(self)->List[float]:
        return self.biases
    def weights(self):
        return self.weights



    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            x = np.dot(w, a)
            x1 = x + b

            x2 = NetworkAmbSensors.sigmoid(x1)
            #x2 = NetworkAmbSensors.tangenteHiperbolica(x1)

            a = x2
            ## a = NetworkAmbSensors.sigmoid(np.dot(w, a) + b)

        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data: n_test = len(test_data)
        n = len(training_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print ("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test))
            else:
                print ("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch, eta):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``mini_batch`` is a list of tuples ``(x, y)``, and ``eta``
        is the learning rate."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            #x = [1]*11
            #y = [0]*2
            #x=np.asarray(x)
            #print(x)
            #y=np.asarray(y)
            #print(y)
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        #print(x)
        #print(y)
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            #print(w)
            #print(activation)
            #print(b)
            z = np.dot(w, activation)+b
            zs.append(z)

            activation = NetworkAmbSensors.sigmoid(z)
            #activation = NetworkAmbSensors.tangenteHiperbolica(z)

            activations.append(activation)
        # backward pass


        delta = self.cost_derivative(activations[-1], y) * \
                NetworkAmbSensors.sigmoid_prime(zs[-1])

        #delta = self.cost_derivative(activations[-1], y) * \
        #        NetworkAmbSensors.tangentHiperbolica_prime(zs[-1])

        nabla_b[-1] = delta
        #print(activations[-2])
        #print(delta)
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in range(2, self.num_layers):
            z = zs[-l]


            sp = NetworkAmbSensors.sigmoid_prime(z)
            #sp = NetworkAmbSensors.tangentHiperbolica_prime(z)

            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [abs(self.feedforward(x)-y) for (x,y) in test_data]

        return sum(x for x in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)
    def copy(self):
        n = NetworkAmbSensors(self.sizes)
        n.biases = self.biases.copy()
        n.weights = self.weights.copy()
        return n
