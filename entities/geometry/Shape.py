from typing import List
from abc import abstractmethod

from entities.geometry.Point2D import Point2D


class Shape(object):
    def __init__(self):
        self._minPoint = None
        self._maxPoint = None

    def modified(self):
        self._minPoint = None
        self._maxPoint = None

    @property
    def minPoint(self) -> Point2D:
        if self._minPoint is None:
            ps = self.points;
            self._minPoint = Point2D(min([p.x for p in ps]), min([p.y for p in ps]))
        return self._minPoint


    @property
    def maxPoint(self) -> Point2D:
        if self._maxPoint is None:
            ps = self.points;
            self._maxPoint = Point2D(max([p.x for p in ps]), max([p.y for p in ps]))
        return self._maxPoint

    @property
    @abstractmethod
    def points(self) -> List[Point2D]:
        raise NotImplementedError

    def overlaps(self, shape) -> bool:
        min1 = self.minPoint
        max1 = self.maxPoint
        min2 = shape.minPoint
        max2 = shape.maxPoint
        if max1.x < min2.x or max1.y < min2.y:
            return False

        if max2.x < min1.x or max2.y < min1.y:
            return False

        return True

