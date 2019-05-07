from typing import List
import math
from OpenGL.GL import *


class Point2D(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def as_list(self) -> List[float]:
        return [self.x, self.y]

    def dot_product(self, other: 'Point2D') -> float:
        return self.x * other.x + self.y * other.y

    def mul_by_value(self, value: float) -> 'Point2D':
        return Point2D(self.x * value, self.y * value)

    def distance_to(self, other: 'Point2D') -> float:
        x_distance = other.x - self.x
        y_distance = other.y - self.y
        return math.sqrt(x_distance * x_distance + y_distance * y_distance)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def unitary(self):
        long = self.length()
        return Point2D(self.x/long, self.y/long)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point2D):
            return False
        return self.x == o.x and self.y == o.y

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __hash__(self) -> int:
        return 31 * hash(self.x) + hash(self.y)

    def __repr__(self) -> str:
        return "Point2D({0}, {1})".format(self.x, self.y)

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.x - other.x, self.y - other.y)

    def __neg__(self) -> 'Point2D':
        return Point2D(-self.x, -self.y)

    def rotate(self, center: 'Point2D', radians: float) -> 'Point2D':
        p = self - center
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Point2D(p.x*cos - p.y*sin + center.x, p.x*sin + p.y*cos + center.y)

    def render(self):
        glVertex3f(self.x, self.y, 0)
