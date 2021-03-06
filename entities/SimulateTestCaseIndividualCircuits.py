import math
import pickle
from entities.carsimulator.Race import Race
from entities.Inici2 import Inici

from entities.ScoreTestCasesTrainingAllCircuits import ScoreTestCases
import numpy as np
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print ('OpenGL wrapper for python not found')


class Scene:

    def __init__(self, num_cars, circuits, has_to_save_car, num_max_simulations, ponderation):
        self._network_best_car = pickle.load(open('../TestCasesNetsTrainingIndividualCircuits/circuit_' + str(circuits[0]) + '_simulation_1.csv', 'rb'))
        print(self._network_best_car)

        self._circuits = circuits
        self._index_circuits = 0

        self._test_circuits = [13, 14, 15]
        self._index_test_circuits = 0
        self._best_car = None  # We'll use it for test the test circuits
        self._index_best_car = None

        self.are_training_circuits_completed = False  # If it's true then we have to test our best car in test circuits

        self._num_cars = num_cars
        self._ponderation = ponderation
        self._total_laps = 2

        self._race = Race(self._circuits[self._index_circuits], num_cars, has_to_save_car, self._ponderation, self._total_laps, self._network_best_car)
        self._car_nets = self._race.get_nets()  # Car's nets of our first circuit

        self._cars_circuits_completed = [0 for i in range(self._num_cars)]
        self._cars_distance = [[] for i in range(self._num_cars)]
        self._cars_distance_accumulated = [0 for i in range(self._num_cars)]
        self._cars_distance_minimum = [999999999 for i in range(self._num_cars)]
        self._cars_weight_treated = [0 for i in range(self._num_cars)]

        self._number_simulations = 1
        self._num_max_simulations = num_max_simulations

        self._aspect_ratio = 1
        self._last_time = 0

    def number_simulations(self):
        return int(self._number_simulations)

    def ponderacio(self):
        return self._ponderation

    def reset_scene(self):
        self._number_simulations = 1
        self.are_training_circuits_completed = False

        print('simulation 1/{0}'.format(self._num_max_simulations))
        self.reset_race_info()
        self._race = Race(self._circuits[self._index_circuits], num_cars, has_to_save_car, self._ponderation, self._total_laps)
        self._car_nets = self._race.get_nets()


    def reset_race_info(self):
        self._last_time = 0

        self._index_circuits = 0
        self._index_test_circuits = 0

        self._cars_circuits_completed = [0 for i in range(self._num_cars)]
        self._cars_distance = [[] for i in range(self._num_cars)]
        self._cars_distance_accumulated = [0 for i in range(self._num_cars)]
        self._cars_distance_minimum = [999999999 for i in range(self._num_cars)]

    def save_best_car_net(self):
        filepath = '../TestCasesNetsTrainingAllCircuits/testcase{0}.csv'.format(self._test_case)
        f = open(filepath, 'wb')
        pickle.dump(self._best_car.net, f)
        f.close()

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)

    def reshape(self, width, height):
        glViewport(0, 0, width, height)
        self._aspect_ratio = width/height

    def get_circuits_from_test_case(self, test_case):
        circuits = []
        for index in range(1, 8, 1):
            mask = 1
            has_circuit = test_case & mask

            if (has_circuit):
                circuits.append(index)

            test_case = (test_case >> 1)

        return circuits

    def get_test_case_from_circuits(self, circuits):
        test_case = 0

        for index, isCircuitEnabled in enumerate(circuits):
            mask = 1

            if isCircuitEnabled:
                mask = (mask << index)
                test_case = test_case | mask

        return test_case

    def draw_car_HUD(self, first_car):
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
        text = "Collision sensors"
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(0.045 * self._aspect_ratio, -0.95)
        text = "Central sensors".format(self._circuits[self._index_circuits])
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if not self.are_training_circuits_completed:

            glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
            text = "Circuit: {0}".format(self._circuits[self._index_circuits])
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        else:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.5)
            text = "Circuit Test: {0}".format( self._test_circuits[self._index_test_circuits] - 12)
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self._ponderation == 1:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderation: d"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self._ponderation == 2:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderation: d^2"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self._ponderation == 3:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderation: v"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        if self._ponderation == 4:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderation: d*v"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))
        if self._ponderation == 5:
            glRasterPos2f(-0.95 * self._aspect_ratio, -0.55)
            text = "Ponderation: d con AG"
            for ch in text:
                glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.6)
        text = "Distance: {0:.2f}".format(first_car.get_total_distance())
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.85)
        text = "Time: {0:.2f}".format(self._race.total_time)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.80)
        text = "Laps: {0}/{1}".format(first_car.laps + 1, self._total_laps)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.75)
        text = "Alives: {0}".format(self._race.alives)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.70)
        if not self.are_training_circuits_completed:
            text = "Simulations: {0}/{1}".format(self._number_simulations, self._num_max_simulations)
        else:
            text = "Simulations: 1/1"

        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

        glRasterPos2f(-0.95 * self._aspect_ratio, -0.65)
        text = "Speed: {0:.2f}, Direction: {1:.2f}".format(first_car.current_speed, first_car.steer)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ctypes.c_int(ord(ch)))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1, 1, 1, 1)
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

        self.draw_car_HUD(first_car)

        glutSwapBuffers()

    def update_best_car(self):
        best_weight = self._cars_weight_treated[0]
        self._best_car = self._race.cars[0]
        self._index_best_car = 0

        index = 0
        for i in range(1, len(self._cars_weight_treated)):
            index += 1
            if best_weight < self._cars_weight_treated[index]:
                best_weight = self._cars_weight_treated[index]
                self._best_car = self._race.cars[index]
                self._index_best_car = index

    def update_cars_net(self):
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

                net_input = np.asarray(net_input)

                r = car._net.feedforward(net_input)
                steer = r[0]
                speed = r[1]
                car.steer = steer[0] - 0.5

                car.rotate((steer[0] - 0.5) * 10 * (2 * math.pi) / 360)
                car.current_speed = 3 + min(3, speed[0] * 3)

        for c in self._race.cars:
            if not c.collision:
                c.collision_time = self._race.total_time

    def update_race(self):
        num_cars_that_completed_circuit = 0
        for index, car in enumerate(self._race.cars):
            car_weight = car.get_weight()
            # Save best distance
            self._cars_distance[index].append(car_weight)
            self._cars_distance_accumulated[index] += car_weight

            if self._cars_distance_minimum[index] > car_weight:
                self._cars_distance_minimum[index] = car_weight

            if(car.laps == self._total_laps):
                num_cars_that_completed_circuit += 1
                self._cars_circuits_completed[index] += 1

            if not car.collision:
                car.collision_time = self._race.total_time

        """
        if (self._race.get_first_car().laps == 2) and (self._best_time is None or self._race.total_time < self._best_time):
            self._best_time = self._race.total_time
        """

        all_races_done = self._index_circuits == (len(self._circuits) - 1)
        if not all_races_done:
            self._index_circuits += 1

        else:  # If we have done last race

            self._number_simulations += 1

            self._cars_weight_treated = [weight * self._cars_distance_minimum[index]
                                         for index, weight in enumerate(self._cars_distance_accumulated)]

            if any(car_circuits_completed == len(self._circuits) for car_circuits_completed in self._cars_circuits_completed)\
                    or self._number_simulations == 1 + self._num_max_simulations:
                self.are_training_circuits_completed = True

                self.update_best_car()
                self._score_test_cases.add_test_case(self._circuits, self._cars_distance[self._index_best_car])
                self._race = Race(self._test_circuits[self._index_test_circuits], 1, has_to_save_car, self._ponderation,
                                  self._total_laps, self._network_best_car)
                self._race.update_nets([self._best_car.net])
                self._last_time = 0
                return

            print("simulation {0}/{1}".format(self._number_simulations, self._num_max_simulations))
            self.reset_race_info()
            self._car_nets = self.particleFilter(self._cars_weight_treated, self._car_nets)

        self._race = Race(self._circuits[self._index_circuits], self._num_cars, has_to_save_car, self._ponderation, self._total_laps, self._network_best_car)
        self._race.update_nets(self._car_nets)

    def idle(self):
        time = glutGet(GLUT_ELAPSED_TIME)

        if self._last_time == 0 or time >= self._last_time + 30:

            elapsed_time = 80/1000

            self.update_cars_net()
            self._race.simulate(elapsed_time)

            if self.are_training_circuits_completed:
                is_race_finished = self._race.all_cars_not_collide_have_finished_laps() or self._race.alives == 0

                if is_race_finished:

                    self._score_test_cases.update_weight_test_circuit(self._test_case, self._index_test_circuits, self._race.cars[0].get_weight())
                    self._index_test_circuits += 1

                    are_all_test_circuits_completed = self._index_test_circuits == len(self._test_circuits)
                    if are_all_test_circuits_completed:

                        self._score_test_cases.print_score()
                        exit(0)

                    self._race = Race(self._test_circuits[self._index_test_circuits], 1, has_to_save_car, self._ponderation, self._total_laps)
                    self._race.update_nets([self._best_car.net])
            else:
                is_race_finished = self._race.all_cars_not_collide_have_finished_laps() or self._race.alives == 0
                if is_race_finished:
                    self.update_race()

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

    def visible(self, vis):
        glutIdleFunc(self.idle)
        """
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)
        """

def main(num_cars, circuits, has_to_save_car, num_max_simulations, ponderation):

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(1000, 900)
    glutInitWindowPosition(0, 0)

    glutCreateWindow(b'Car Machine Learning')

    scene = Scene(num_cars, circuits, has_to_save_car, num_max_simulations, ponderation)

    scene.init()

    glutDisplayFunc(scene.display)
    glutReshapeFunc(scene.reshape)
    glutVisibilityFunc(scene.visible)

    glutMainLoop()

windows = Inici()
windows.start()

if __name__ == '__main__':
        has_to_save_car = 0  # si és 1 se guarda en UsuariCircuit el cotxe inicial
        ponderation = 1 # d^2
        num_cars = 1
        num_max_simulations = 1
        circuits = windows.getCircuits()

        # Error to get circuits
        if not circuits:
            print("Error to get individual circuit.")
            exit(0)

        main(num_cars, circuits, has_to_save_car, num_max_simulations, ponderation)