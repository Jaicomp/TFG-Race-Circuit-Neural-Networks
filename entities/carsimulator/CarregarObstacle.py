
from entities.geometry.Point2D import Point2D
class CarregarObstacle:
    def __init__(self,n):
        self.__lista = []

        if n == 8:
            self.__lista.append([Point2D(36, 23), Point2D(30, 23), Point2D(33, 19),Point2D(36, 19)])
            self.__lista.append([Point2D(60, 20), Point2D(66, 20), Point2D(66, 26), Point2D(60, 26)])
            self.__lista.append([Point2D(127, 60), Point2D(129, 53), Point2D(131, 56)])
            self.__lista.append([Point2D(60, 100), Point2D(64, 100), Point2D(64, 103), Point2D(62, 103)])
            self.__lista.append([Point2D(60, 43), Point2D(64, 44), Point2D(64, 45), Point2D(60, 51)])
            self.__lista.append([Point2D(82, 106), Point2D(96, 104), Point2D(93, 108)])



        if n == 10:
            self.__lista.append([Point2D(38, 102), Point2D(44, 106), Point2D(64, 103)])
            self.__lista.append([Point2D(72, 75), Point2D(79, 75), Point2D(76, 70)])
            self.__lista.append([Point2D(106, 20), Point2D(110, 18), Point2D(112, 23), Point2D(109, 27), Point2D(105, 26)])


        if n == 3:
            self.__lista.append([Point2D(70, 122), Point2D(85, 120), Point2D(70, 115)])
            self.__lista.append([Point2D(70, 103), Point2D(85, 103), Point2D(70, 110)])

        if n==12:
            self.__lista.append([Point2D(70,-9),Point2D(50,-1),Point2D(40,-7),Point2D(40,-9),Point2D(55,-12)])

            self.__lista.append([Point2D(70, -18), Point2D(55, -27),Point2D(40,-18),Point2D(55,-16)])
            self.__lista.append([Point2D(30,-23),Point2D(36,-30),Point2D(46,-28),Point2D(40,-24),Point2D(35,-20)])
            self.__lista.append([Point2D(29,79),Point2D(36,83),Point2D(50,79)])
            self.__lista.append([Point2D(32,75),Point2D(36,71),Point2D(50,75)])
            self.__lista.append([Point2D(30, 95), Point2D(36, 91), Point2D(40, 95),Point2D(36, 100)])
            self.__lista.append([Point2D(45, 105), Point2D(66, 115),Point2D(80, 116), Point2D(90, 105), Point2D(66, 101)])

        if n==15:
            self.__lista.append([Point2D(56, 47), Point2D(72, 44), Point2D(55, 57)])
            self.__lista.append([Point2D(120, 85), Point2D(127, 90), Point2D(129, 77),Point2D(120,78)])


    def lista(self):
        return self.__lista
