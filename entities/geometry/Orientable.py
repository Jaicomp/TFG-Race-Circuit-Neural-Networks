from abc import abstractmethod


class Orientable:

    @abstractmethod
    def rotate(self, rotation_in_radians: float):
        """Rotate counter-clockwise. Use negative rotation to rotate clockwise."""
        raise NotImplementedError

    @property
    @abstractmethod
    def rotation_in_radians(self) -> float:
        raise NotImplementedError
