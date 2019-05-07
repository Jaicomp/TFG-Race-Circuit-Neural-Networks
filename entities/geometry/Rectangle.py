from typing import List
import math

# from entities.geometry import Point2D, Shape, Positionable, Orientable
from entities.geometry.Point2D import Point2D
from entities.geometry.Shape import Shape
from entities.geometry.Positionable import Positionable
from entities.geometry.Orientable import Orientable


class Rectangle(Shape, Positionable, Orientable):

    def __init__(self, width: float, height: float):
        super(Rectangle, self).__init__()
        self.__position = Point2D(0, 0)
        self.__rotation_in_radians = 0
        self.__center = Point2D(0, 0)
        self.width = width
        self.height = height


    @property
    def points(self) -> List[Point2D]:
        p1 = self.__position + Point2D(-self.width/2, -self.height/2)
        p2 = self.__position + Point2D( self.width/2, -self.height/2)
        p3 = self.__position + Point2D( self.width/2,  self.height/2)
        p4 = self.__position + Point2D(-self.width/2,  self.height/2)

        return [p1.rotate(self.__position, self.__rotation_in_radians),
                p2.rotate(self.__position, self.__rotation_in_radians),
                p3.rotate(self.__position, self.__rotation_in_radians),
                p4.rotate(self.__position, self.__rotation_in_radians)
                ]

    @property
    def position(self) -> Point2D:
        """Returns the left point of the rectangle (middle point of two left corners"""
        return self.__position

    @position.setter
    def position(self, new_position: Point2D):
        self.__position = new_position
        self.modified()

    @property
    def center(self) -> Point2D:
        return self.__center

    @center.setter
    def center(self, new_center: Point2D):
        self.__center = new_center

    def rotate(self, rotation_in_radians: float):
        self.__rotation_in_radians += rotation_in_radians
        self.modified()

    @property
    def rotation_in_radians(self) -> float:
        return self.__rotation_in_radians

    @rotation_in_radians.setter
    def rotation_in_radians(self, new_rotation_in_radians: float):
        self.__rotation_in_radians = new_rotation_in_radians
