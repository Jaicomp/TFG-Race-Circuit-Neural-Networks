from usecases.drivecar.interactor import InputBoundary, DataAccessInterface


class Interactor(InputBoundary):
    __MAX_ACCELERATION_INCREMENT_IN_METERS_PER_SEC = 1
    __MAX_DECELERATION_INCREMENT_IN_METERS_PER_SEC = 2
    __MIN_WHEEL_ROTATION_IN_DEGREES = -45
    __MAX_WHEEL_ROTATION_IN_DEGREES = 45
    __WHEEL_ROTATION_RANGE = __MAX_WHEEL_ROTATION_IN_DEGREES - __MIN_WHEEL_ROTATION_IN_DEGREES

    def __init__(self, data_accessor: DataAccessInterface):
        self.__data_accessor = data_accessor

    def accelerate(self, acceleration_factor: float):
        car = self.__data_accessor.get_car()
        speed_increment = self.__MAX_ACCELERATION_INCREMENT_IN_METERS_PER_SEC * acceleration_factor
        new_speed = car.speed_in_meters_per_sec + speed_increment
        car.speed_in_meters_per_sec = new_speed
        self.__data_accessor.update_car(car)

    def brake(self, deceleration_factor: float):
        car = self.__data_accessor.get_car()
        speed_decrement = self.__MAX_DECELERATION_INCREMENT_IN_METERS_PER_SEC * deceleration_factor
        new_speed = car.speed_in_meters_per_sec - speed_decrement
        car.speed_in_meters_per_sec = new_speed
        self.__data_accessor.update_car(car)

    def turn_wheels(self, steering_wheel_rotation_factor: float):
        car = self.__data_accessor.get_car()
        rotation_offset = self.__WHEEL_ROTATION_RANGE * steering_wheel_rotation_factor
        car.wheels_rotation_in_degrees = self.__MIN_WHEEL_ROTATION_IN_DEGREES + rotation_offset
        self.__data_accessor.update_car(car)
