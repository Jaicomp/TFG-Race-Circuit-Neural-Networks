from abc import abstractmethod


class InputBoundary:

    @abstractmethod
    def accelerate(self, acceleration_factor: float):
        raise NotImplementedError

    @abstractmethod
    def brake(self, deceleration_factor: float):
        raise NotImplementedError

    @abstractmethod
    def turn_wheels(self, steering_wheel_rotation_factor: float):
        """
        0 (or negative) means steering wheel is fully turned right
        1 (or higher) means steering wheel is fully turned left
        """
        raise NotImplementedError
