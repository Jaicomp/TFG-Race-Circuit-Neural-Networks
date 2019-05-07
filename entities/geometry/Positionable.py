from abc import abstractmethod

from entities.geometry import Point2D


class Positionable:

    @property
    @abstractmethod
    def position(self) -> Point2D:
        raise NotImplementedError

    @position.setter
    @abstractmethod
    def position(self, new_position: Point2D):
        raise NotImplementedError