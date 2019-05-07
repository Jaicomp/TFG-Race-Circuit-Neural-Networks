import math
import os
import pickle
from enum import Enum
from entities.carsimulator.Race import Race
from entities.carsimulator.Car import Car

from entities.Inici import Inici
from entities.neuralnetwork.Network import Network
from entities.guardar30xarxes import guardar30xarxes
from entities.load30xarxes import load30xarxes
import numpy as np
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print ('OpenGL wrapper for python not found')

class WeightTreatment():
    ADD_WEIGHTS = 0
    MULT_LOWER_WEIGHT = 1

    @staticmethod
    def add_weights(weights):
        total_weight = 0
        for weight in weights:
            total_weight += weight

        return total_weight

    @staticmethod
    def mult_lower_weight(weights):
        total_weight = 0
        lower_weight = 99999999
        for weight in weights:
            if weight < lower_weight:
                lower_weight = weight

            total_weight += weight

        return total_weight * lower_weight



class Scene:

    def __init__(self, circuit, cotxes, has_to_save_car, network_cars, simulacions, ponderacio, de_facil_a_dificil):
        self._circuits = [1, 2]
        self._index_circuits = 0

        self.weight_treatments = [WeightTreatment.ADD_WEIGHTS, WeightTreatment.MULT_LOWER_WEIGHT]
        self.weight_treatments_index = 0

        self._total_laps = 2

        self._num_iterations_by_frame = 100
        self._counter_iterations = 0

        self.__circuit = circuit

        self.__de_facil_a_dificil = de_facil_a_dificil
        self.__ponderacio = ponderacio

        self._race = Race(self._circuits[self._index_circuits], cotxes, has_to_save_car, network_cars, self.__ponderacio, self._total_laps)

        self.car_nets = self._race.get_nets() # Car's nets of our first circuit
        self._cars_best_distance = [[] for i in range(cotxes)]
        self._cars_circuits_completed = [0 for i in range(cotxes)]

        self._aspect_ratio = 1
        self._number_simulations = 1
        self._best_time = None
        self._simulacions = simulacions
        self._net_input = None
        self.__cotxes = cotxes
        self._last_time = 0

    def number_simulations(self):
        return int(self._number_simulations)

    def ponderacio(self):
        return self.__ponderacio

    def reset_race(self):
        if self._simulacions != 1:
            self._race.reset()
        self._number_simulations = self._number_simulations + 1

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        self._aspect_ratio = width/height

    def display(self):
        """
        if self._counter_iterations > 0:
            return
        print("IM IN")
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self._aspect_ratio, 1, 1501)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        first_car = self._race.get_first_car()

        gluLookAt(first_car.position.x, first_car.position.y, 120,
                  first_car.position.x, first_car.position.y, 0,
                  0, 1, 0)
        glEnable(GL_DEPTH_TEST)

        self._race.render()

        # Visualitzar el circuit sense cotxes
        ######################################################################################################################

        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glClearColor(1,1,1,1)
        # px = 45
        # py = 50
        # glLoadIdentity()
        # gluLookAt(px, py, 270,
        #           px, py, 0,
        #           0, 1, 0)
        # self._race.track.render2()
        # glutSwapBuffers()
        # return
        #####################################################################################################################

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1*self._aspect_ratio, 1*self._aspect_ratio, -1, 1, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)

        glColor3f(1, 1, 1)
        width_bar = 0.01
        x = -len(first_car.collision_distances) / 2 * width_bar - 0.2
        # BARRAS DE TODOS LOS SENSORES
        for dis in first_car.collision_distances:
            y1 = -0.9
            y2 = y1 + dis / 150
            glBegin(GL_QUADS)
            glColor3f(first_car.body_colors[0], first_car.body_colors[1], first_car.body_colors[2])
            glVertex3f(x, y1, 0)
            glVertex3f(x, y2, 0)
            glVertex3f(x + width_bar * 0.95, y2, 0)
            glVertex3f(x + width_bar * 0.95, y1, 0)
            glEnd()
            x = x + width_bar

        glColor3f(1, 1, 1)
        width_bar = 0.01
        x = -len(first_car.collision_distances) / 2 * width_bar + 0.2
        # BARRAS DEL SENSOR CENTRAL

        if first_car.carTemps() < 101:
            distances_central_sensor = first_car.sensorCentral()
        else:
            v = []
            for i in range(10):
                v.append(first_car.memoriaSensorCentral()[(first_car.carTemps()-1) - i * 10])
            v.reverse()
            distances_central_sensor = v

        for dis in distances_central_sensor:
            y1 = -0.9
            y2 = y1 + dis / 150
            glBegin(GL_QUADS)
            glColor3f(first_car.body_colors[0], first_car.body_colors[1], first_car.body_colors[2])
            glVertex3f(x, y1, 0)
            glVertex3f(x, y2, 0)
            glVertex3f(x + width_bar * 0.95, y2, 0)
            glVertex3f(x + width_bar * 0.95, y1, 0)
            glEnd()
            x = x + width_bar

        glRasterPos2f(-0.15 * self._aspect_ratio, -0.95)
        text = "Sensores"
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(0.045 * self._aspect_ratio, -0.95)
        text = "S. central".format(self.__circuit)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__circuit in range(1, 13):

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
            text = "Circuit: {0}".format(self.__circuit)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        else:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
            text = "Circuit Test: {0}".format(self.__circuit - 12)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__ponderacio == 1:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderació: d"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__ponderacio == 2:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderació: d^2"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__ponderacio == 3:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderació: v"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__ponderacio == 4:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderació: d*v"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self.__ponderacio == 5:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderació: d con AG"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__de_facil_a_dificil == 0:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "De fàcil a difícil: Si"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self.__de_facil_a_dificil == 1:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
            text = "De fàcil a difícil: No"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.9)
        text = "Distància: {0:.2f}".format(first_car.get_total_distance())
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.85)
        if self._best_time is not None:
            text = "Temps i MillorTemps: {0:.2f},{1:.2f}".format(self._race.total_time, self._best_time)
        else:
            text = "Temps: {0:.2f}".format(self._race.total_time)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.80)
        text = "Voltes: {0}".format(first_car.laps + 1)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.75)
        text = "Vius: {0}".format(self._race.alives)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.70)
        text = "Simulacions: {0}/{1}".format(self._number_simulations, self._simulacions)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.65)
        text = "Valors {0:.2f}, {1:.2f}".format(first_car.current_speed, first_car.steer)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
            # glRasterPos2f(-0.95*self._aspect_ratio, -0.65)
            # text = "Velocitat i direcció: {0:.2f}".format(first_car.current_speed)
            # for ch in text:
            #   glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int( ord(ch)))

        glutSwapBuffers()

    def special(self, key, x, y):
        if key == GLUT_KEY_END:
            #sys.exit()
            self.reset_race()

    def specialUp(self, key, x, y):
        pass

    def idle(self):
        time = glutGet(GLUT_ELAPSED_TIME)
        """
        if self._number_simulations == 1 + self._simulacions:
            xarxes=[]
            for i in range(self.__cotxes):
                xarxes.append(self._race.cars[i].net)
            #guardar30xarxes(xarxes,self.__ponderacio,self.__de_facil_a_dificil)

            exit(0)
        """
        if self._last_time == 0 or time >= self._last_time + 30:
            """
            self._counter_iterations += 1

            if self._counter_iterations >= self._num_iterations_by_frame:
                self._counter_iterations = 0
            """

            #elapsed_time = (time-last_time)/1000
            elapsed_time = 80/1000

            for car in self._race.cars:
                if not car.collision:
                    net_input = []
                    for i in car.collision_distances:
                        net_input.append([i])

                    car.memoriaSensorCentral().append(net_input[5][0])
                    if car.carTemps() < 100:
                        car.sensorCentral().append(net_input[5][0])
                        car.sensorCentral().pop(0)
                        for i in car.sensorCentral():
                            net_input.append([i])
                    else:
                        v = []
                        for i in range(10):
                            v.append(car.memoriaSensorCentral()[car.carTemps() - i * 10])
                        v.reverse()
                        for i in v:
                            net_input.append([i])

                    self._net_input = net_input

                    net_input = np.asarray(net_input)

                    r = car._net.feedforward(net_input)
                    steer = r[0]
                    speed = r[1]
                    car.steer = steer[0]-0.5

                    car.rotate((steer[0]-0.5) * 10*(2*math.pi)/360)
                    car.current_speed = 3 + min(3, speed[0] * 3)

            self._race.simulate(elapsed_time)

            for c in self._race.cars:
                if not c.collision:
                    c.collision_time = self._race.total_time

            if self._race.all_cars_not_collide_have_finished_laps() or self._race.alives == 0:
                num_cars_that_completed_circuit = 0
                for index, car in enumerate(self._race.cars):
                    # Save best distance
                    self._cars_best_distance[index].append(car.get_weight())

                    if(car.laps == self._total_laps):
                        num_cars_that_completed_circuit += 1
                        self._cars_circuits_completed[index] += 1

                    if not car.collision:
                        car.collision_time = self._race.total_time
                print(num_cars_that_completed_circuit)
                print(self._cars_circuits_completed)
                print("BEST DISTANCES: ", self._cars_best_distance)
                """
                if (self._race.get_first_car().laps == 2) and (self._best_time is None or self._race.total_time < self._best_time):
                    self._best_time = self._race.total_time
                """

                all_races_done = self._index_circuits == (len(self._circuits) - 1)
                if not all_races_done:
                    self._index_circuits += 1

                else:  # If we have done last race

                    if any(car_circuits_completed == len(self._circuits) for car_circuits_completed in self._cars_circuits_completed):
                        print("A CAR HAS COMPLETED ALL CIRCUITS")
                        print("SIMULATIONS: ", self._number_simulations)
                        exit(0)

                    self._number_simulations += 1
                    if self._number_simulations == 1 + self._simulacions:
                        print("ACABAO")
                        exit(0)

                    self._index_circuits = 0

                    weights_operated = self.apply_weight_treatment(self._cars_best_distance)

                    print("WEIGHTS OPPERATED: ", weights_operated)

                    self.car_nets = self.particleFilter(weights_operated, self.car_nets)
                    self._last_time = 0
                    self._cars_best_distance = [[] for i in range(cotxes)]
                    self._cars_circuits_completed = [0 for i in range(cotxes)]

                self._race = Race(self._circuits[self._index_circuits], cotxes, has_to_save_car, network_cars, self.__ponderacio, self._total_laps)
                self._race.update_nets(self.car_nets)

            self._last_time = time
            glutPostRedisplay()

    def particleFilter(self, weights, previous_nets):
        nets = []

        percent_cars_to_reuse = 5  # %
        num_best_nets_to_reuse = int((percent_cars_to_reuse / 100.0) * len(weights))

        higher_weights_indexes = []
        higher_weights = []

        # Particle filter doesn't work for genetic algorithm.
        total_weight = 0
        sum_weights = []
        for index, weight in enumerate(weights):
            total_weight = total_weight + weight
            sum_weights.append(total_weight)

            if num_best_nets_to_reuse != len(higher_weights_indexes):
                higher_weights_indexes.append(index)
                higher_weights.append(weight)
            else:
                is_new_higher_weight = False
                last_high_weight = 999999999

                for higher_weight_index, higher_weight in enumerate(higher_weights):

                    if (weight > higher_weight and higher_weight < last_high_weight):
                        last_high_weight_index = higher_weight_index
                        last_high_weight = higher_weight

                        new_high_weight_index = index
                        new_high_weight = weight

                        is_new_higher_weight = True

                if (is_new_higher_weight):
                    higher_weights[last_high_weight_index] = new_high_weight
                    higher_weights_indexes[last_high_weight_index] = new_high_weight_index

        for index in higher_weights_indexes:
            nets.append(previous_nets[index].copy())

        for previous_net in range(num_best_nets_to_reuse, len(previous_nets)):
            index = 0
            weight_found = False
            random_weight = np.random.uniform(0, total_weight)

            while index < len(sum_weights) and not weight_found:

                if random_weight <= sum_weights[index]:
                    weight_found = True
                else:
                    index += 1

            net = previous_nets[index].copy()
            net.apply_noise()

            nets.append(net)

        return nets

    def apply_weight_treatment(self, weights_all_cars):
        weights_result = []

        weight_treatments = {
            WeightTreatment.ADD_WEIGHTS: WeightTreatment.add_weights,
            WeightTreatment.MULT_LOWER_WEIGHT: "bye"
        }

        weight_treatment_method = weight_treatments.get(self.weight_treatments_index)
        print(WeightTreatment.ADD_WEIGHTS)
        print(weight_treatment_method)
        for weights_car in weights_all_cars:
            weights_result.append(weight_treatment_method(weights_car))

        return weights_result

    def visible(self, vis):
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)


def main(circuit, cotxes, has_to_save_car, network_cars, simulacions, ponderacio, de_facil_a_dificil):

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(0, 0)

    glutCreateWindow(b'Car Machine Learning')

    scene = Scene(circuit, cotxes, has_to_save_car, network_cars, simulacions, ponderacio, de_facil_a_dificil)

    scene.init()

    glutDisplayFunc(scene.display)
    glutReshapeFunc(scene.reshape)
    glutVisibilityFunc(scene.visible)
    glutSpecialFunc(scene.special)
    glutSpecialUpFunc(scene.specialUp)

    glutMainLoop()


def eleccio_del_cotxe(ponderacion, de_facil_a_dificil):

    if ponderacion == 1 and de_facil_a_dificil == 0:
        return int(27)
    if ponderacion == 2 and de_facil_a_dificil == 0:
        return int(30)
    if ponderacion == 3 and de_facil_a_dificil == 0:
        return int(12)
    if ponderacion == 4 and de_facil_a_dificil == 0:
        return int(15)
    if ponderacion == 5 and de_facil_a_dificil == 0:
        return int(7)
    if ponderacion == 1 and de_facil_a_dificil == 1:
        return int(14)
    if ponderacion == 2 and de_facil_a_dificil == 1:
        return int(16)
    if ponderacion == 3 and de_facil_a_dificil == 1:
        return int(19)
    if ponderacion == 4 and de_facil_a_dificil == 1:
        return int(19)
    if ponderacion == 5 and de_facil_a_dificil == 1:
        return int(28)

""" I DON'T NEED IT FOR NOW 
finestra=Inici()
finestra.start()
circuit=finestra.circuit()
ponderacio=finestra.ponderacion()
de_facil_a_dificil=finestra.de_facil_a_dificil()
cotxes=finestra.cotxes()
simulacions=1
usuari=finestra.usuari()

"""
circuit = 1
ponderacio = 2
cotxes = 100
de_facil_a_dificil = 0
simulacions = 5

network_cars = []
"""
if usuari == 1:  # Human doesn't play
    if cotxes != 1:
        network_cars = load30xarxes(ponderacio, de_facil_a_dificil).xarxa()
    else:
        network_cars = [load30xarxes(ponderacio, de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio, de_facil_a_dificil)-1)]
else:
    cotxes = 2
    network_cars.append(load30xarxes(ponderacio, de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio, de_facil_a_dificil)-1))
    network_cars.append(load30xarxes(ponderacio, de_facil_a_dificil).xarxa_cotxe_n(eleccio_del_cotxe(ponderacio, de_facil_a_dificil)-1))
"""
if __name__ == '__main__':
        has_to_save_car = 0  # si és 1 se guarda en UsuariCircuit el cotxe inicial

        main(circuit, cotxes, has_to_save_car, network_cars, simulacions, ponderacio, de_facil_a_dificil)
