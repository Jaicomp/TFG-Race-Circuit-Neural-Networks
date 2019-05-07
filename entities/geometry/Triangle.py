from typing import List

# from entities.geometry import Shape, Point2D
from entities.geometry.Shape import Shape
from entities.geometry.Point2D import Point2D


class Triangle(Shape):

    def __init__(self, v1: Point2D, v2: Point2D, v3: Point2D):
        super(Triangle, self).__init__()
        self.__points = [v1, v2, v3]

    @property
    def points(self) -> List[Point2D]:
        return self.__points

    def area(self):
        v1 = self.points[0]
        v2 = self.points[1]
        v3 = self.points[2]
        return abs((v1.x * (v2.y - v3.y) +
                    v2.x * (v3.y - v1.y) +
                    v3.x * (v1.y - v2.y)) / 2.0)

    def contains(self, point: Point2D) -> bool:
        v1 = self.points[0]
        v2 = self.points[1]
        v3 = self.points[2]
        a = self.area()
        a1 = Triangle(point, v2, v3).area()
        a2 = Triangle(v1, point, v3).area()
        a3 = Triangle(v1, v2, point).area()
        return a == (a1 + a2 + a3)
