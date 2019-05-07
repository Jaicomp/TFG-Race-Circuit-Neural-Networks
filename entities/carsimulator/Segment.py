from entities.geometry.Point2D import Point2D
from entities.geometry.Polygon import Polygon
from entities.carsimulator.Car import Car
from entities.geometry.CollisionDetection import *
from OpenGL.GL import *
import math


class Segment(object):
    def __init__(self, p1: Point2D, p2: Point2D, p3: Point2D, p4: Point2D, lateral_width: float):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4
        self._lateral_width = lateral_width
        self._pb1 = p1 - (p2-p1).unitary().mul_by_value(lateral_width)
        self._pb2 = p2 - (p1-p2).unitary().mul_by_value(lateral_width)
        self._pb3 = p3 - (p4-p3).unitary().mul_by_value(lateral_width)
        self._pb4 = p4 - (p3-p4).unitary().mul_by_value(lateral_width)

        self._collisionRegions = []
        self._collisionRegions.append(Polygon([self._p1, self._pb1, self._pb3, self._p3]))
        self._collisionRegions.append(Polygon([self._p2, self._pb2, self._pb4, self._p4]))

        self._point_ini = (self.p1 + self.p2).mul_by_value(0.5)
        self._point_end = (self.p3 + self.p4).mul_by_value(0.5)
        self._direction = self._point_end - self.point_ini
        self._total_distance = (self._point_end-self._point_ini).length()



    @property
    def total_distance(self) -> float:
        return self._total_distance

    @property
    def collisionRegions(self) -> List[Polygon]:
        return self._collisionRegions



    @property
    def point_ini(self) -> Point2D:
        return self._point_ini

    @property
    def point_end(self) -> Point2D:
        return self._point_end

    @property
    def direction(self) -> Point2D:
        return self.direction

    @property
    def p1(self) -> Point2D:
        return self._p1

    @property
    def p2(self) -> Point2D:
        return self._p2

    @property
    def p3(self) -> Point2D:
        return self._p3

    @property
    def p4(self) -> Point2D:
        return self._p4

    def __repr__(self) -> str:
        return "P1({0}, {1})".format(self.p1.x, self.p1.y)

    def collides(self, car: Car) -> bool:
        carBounding = car.bounds
        for cr in self._collisionRegions:
            if are_colliding(cr, carBounding):
                return True


    def render(self):
        for cr in self._collisionRegions:
            glColor3f(1, 1, 1)
            glBegin(GL_LINE_LOOP)
            for p in cr.points:
                p.render()
            glEnd()

    def render2(self):
        for cr in self._collisionRegions:
            glColor3f(0, 0, 0)
            glBegin(GL_LINE_LOOP)
            for p in cr.points:
                p.render()
            glEnd()





    def in_segment(self, point: Point2D) -> bool:
        return inside_polygon(point, [self._p1, self._p3, self._p4, self._p2])

    def advanced(self, point: Point2D) -> Point2D:
        projection_point = line_intersection(self.p1, self.p2, self.p3, self.p4)

        if projection_point is None:
            # Consideramos que el principio y el fin son paralelas
            width_ini = (self.p2 - self.p1).length()
            width_end = (self.p4 - self.p3).length()

            width_max = max(width_ini, width_end)

            v = self._direction.unitary()
            v = Point2D(v.y, -v.x).mul_by_value(width_max * 2)
            point_a = point + v
            point_b = point - v

            intersection = segment_intersection(self._point_ini, self._point_end, point_a, point_b)
            return intersection
        else:
            # no son paralelas
            return line_intersection(projection_point, point, self._point_ini, self._point_end)

    def get_start_position(self) -> (Point2D, float):
        return (self.point_ini, math.atan2(self._direction.y, self._direction.x))





