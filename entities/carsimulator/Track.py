from typing import List
from entities.geometry.Point2D import Point2D
from entities.carsimulator.Segment import Segment
from entities.carsimulator.ObstaculoCuadrilatero import Obstaculo
from entities.geometry.Polygon import Polygon
from entities.carsimulator.CarregarCircuit import CarregarCircuit
from entities.carsimulator.CarregarObstacle import CarregarObstacle
from OpenGL.GL import *
import csv
import os


class Track(object):
    def __init__(self, circuit):

            self.__points = CarregarCircuit(circuit).points()
            widths = CarregarCircuit(circuit).widths()

            self._segments = []
            parray = []
            for i in range(0, len(self.__points)):
                p0 = self.__points[i]
                j = (i + 1) % len(self.__points)
                p1 = self.__points[j]
                k = (i + 2) % len(self.__points)
                p2 = self.__points[k]
                v0 = (p1 - p0).unitary()
                v1 = (p2 - p1).unitary()
                vf = (v0 + v1).unitary()
                vn = Point2D(vf.y, -vf.x)
                width = widths[i]
                pn1 = p1 + vn.mul_by_value(width)
                pn2 = p1 - vn.mul_by_value(width)
                parray.append((pn1, pn2))

            wall_width = 0.5
            for i in range(0, len(parray)):
                j = (i+1) % len(parray)
                p0 = parray[i][0]
                p1 = parray[i][1]
                p2 = parray[j][0]
                p3 = parray[j][1]
                self._segments.append(Segment(p0, p1, p2, p3, wall_width))

            obstacles = CarregarObstacle(circuit).lista()
            for i in obstacles:
                self._segments[0].collisionRegions.append(Polygon(i))

    def DistanciaTotalCircuit(self):
        distancia=0

        for i in range(0, len(self.__points)-1):
            distancia=distancia+self.__points[i].distance_to(self.__points[i+1])

        distancia=distancia+self.__points[len(self.__points)-1].distance_to(self.__points[0])

        return distancia

    def render(self):
        for s in self._segments:
            s.render()

    def render2(self):
        for s in self._segments:
            s.render2()

    def next_segment(self, num: int) -> int:
        return (num + 1) % len(self.segments)

    def previous_segment(self, num: int) -> int:
        return (num - 1 + len(self.segments)) % len(self.segments)

    @property
    def segments(self) -> List[Segment]:
        return self._segments

    def get_start_position(self) -> (Point2D, float, int):
        '''
        Compute start position in the track
        :return: Three values: Start Position, Orientation, Starting Segment Index
        '''
        start_segment = 0
        a = self.segments[start_segment].get_start_position()
        return a[0], a[1], start_segment




