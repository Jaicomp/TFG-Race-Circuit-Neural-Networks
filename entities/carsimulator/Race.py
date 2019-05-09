from entities.carsimulator.Track import Track
from entities.carsimulator.Car import Car
from entities.geometry.CollisionDetection import *
from entities.neuralnetwork.Network import Network
from OpenGL.GL import *
import numpy

class Race(object):
    def __init__(self, circuit, cotxes, has_to_save_car, ponderacio, total_laps):
        self.__ponderacio = ponderacio
        self._track = Track(circuit)
        self._cars = []
        self.__circuit = circuit
        self.__number_cars = cotxes
        self.__total_time = 0
        self.__alives = self.__number_cars
        # inicializacion de coches
        self.__has_to_save_car = has_to_save_car
        self.__total_time = 0
        self._total_laps = total_laps

        for x in range(0, self.__number_cars):

            # car = Car(self._track, 2, 1, Point2D(-1, 0), is_player, circuit, network_cars[x], self.__ponderacio)
            car = Car(self._track, 2, 1, Point2D(-1, 0), self.__ponderacio)
            start_position, angle, start_segment = self._track.get_start_position()
            car.bounds.position = start_position
            car.bounds.rotation_in_radians = angle
            car.current_segment = start_segment
            car.distance = 0
            car.number = x

            self._cars.append(car)

    def get_first_car(self) -> Car:
        max_distance = None
        first_car = self._cars[0]
        for c in self._cars:
            distance = c.get_total_distance()
            if (not c.collision and ((max_distance is None) or (distance > max_distance))):
                max_distance = distance
                first_car = c
        return first_car

    def render(self):

        for x in range(0, self.__number_cars):
           c=self._cars[x]
           if not c.collision:
                 # Pintar los sensores de los coches
                 for cc in c.collision_points:
                     glBegin(GL_LINES)
                     #glColor3f(1, 1, 1)
                     glColor3f(c.body_colors[0], c.body_colors[1], c.body_colors[2])
                     glVertex3f(cc.x - 1, cc.y - 1, 0)
                     glVertex3f(cc.x + 1, cc.y + 1, 0)
                     glVertex3f(cc.x - 1, cc.y + 1, 0)
                     glVertex3f(cc.x + 1, cc.y - 1, 0)
                     glEnd()

        # renderizamos el circuito
        self._track.render()

        for x in range(0, self.__number_cars):
            self._cars[x].render()

    def simulate(self, elapsed_time: float):
        self.__total_time = self.__total_time + elapsed_time
        for c in self._cars:

            # Car is bugged when it's spinning around himself
            is_car_bugged = self.__total_time > 10.0 and self.__total_time > c.get_total_distance()
            has_traversed_all_laps = c.laps == self._total_laps

            if not c.collision and (is_car_bugged or has_traversed_all_laps):
                c.collision = True;
                self.__alives = self.__alives - 1
                continue

            if not c.collision:
                c.simulate(elapsed_time)

                # miramos si ha habido colision
                for segment in self._track._segments:
                    if segment.collides(c):
                        c.collision = True
                        c.collision_time = self.__total_time

                if c.collision:
                    self.__alives = self.__alives - 1

                # determinamos si hay cambio de segmento (al siguiente o al anterior)
                # y calculamos la distancia total recorrido por los segmentos atravesados
                ns = self._track.next_segment(c.current_segment)
                if self.track.segments[ns].in_segment(c.bounds.position):
                    c.total_segment_distance = c.total_segment_distance + self.track.segments[c.current_segment].total_distance
                    c.current_segment = ns
                    if ns == 0:
                        c.laps = c.laps + 1
                else:
                    ps = self._track.previous_segment(c.current_segment)
                    if self.track.segments[ps].in_segment(c.bounds.position):
                        if c.current_segment == 0:
                            c.laps = c.laps - 1
                        c.current_segment = ps
                        c.total_segment_distance = c.total_segment_distance - self.track.segments[c.current_segment].total_distance

                # distancia recorrida en el segmento actual
                cs = self.track.segments[c.current_segment]
                c.distance = (cs.point_ini - cs.advanced(c.bounds.position)).length()
        if self.__has_to_save_car==1:
            self._cars[0].torna()
            self._cars[0].sensors()

    def get_nets(self) -> List[Network]:
        nets = []
        for car in self._cars:
            nets.append(car.net)
        return nets

    def update_nets(self, nets):
        for index, net in enumerate(nets):
            self._cars[index].update_net(net)

    @property
    def cars(self) -> List[Car]:
        return self._cars

    @property
    def alives(self) -> int:
        return self.__alives

    @property
    def track(self) -> Track:
        return self._track

    @property
    def alives(self) -> int:
        return self.__alives

    @property
    def total_time(self) -> float:
        return self.__total_time

    def total__time(self):
        return self.__total_time

    def all_cars_not_collide_have_finished_laps(self):

        for car in self._cars:
            if not car.collision and car.laps != self._total_laps:
                return False

        return True
