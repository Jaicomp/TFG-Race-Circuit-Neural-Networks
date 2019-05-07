from abc import abstractmethod

from entities import Car


class DataAccessInterface:

    @abstractmethod
    def get_car(self) -> Car:
        raise NotImplementedError

    @abstractmethod
    def update_car(self, car: Car):
        raise NotImplementedError
