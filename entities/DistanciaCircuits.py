from entities.carsimulator.Track import Track
from entities.geometry.Point2D import Point2D

class DistanciaCircuits(object):
    def __init__(self):
        self.__distancies = []
        for i in range(1,16):
            self.__distancies.append(Track(i).DistanciaTotalCircuit())

    def distancies(self):
        return self.__distancies



Distancia=DistanciaCircuits()
print(Distancia.distancies())
for i in range(1,16):
    print("Circuit "+str(i)+" té distància total de "+str(Distancia.distancies()[i-1]))
