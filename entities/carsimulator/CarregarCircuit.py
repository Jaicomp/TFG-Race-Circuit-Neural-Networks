import csv
import os
from entities.geometry.Point2D import Point2D
from openpyxl import load_workbook
class CarregarCircuit:
    def __init__(self,circuit):
        self.__points = []
        self.__widths = []

        dir_path = os.path.dirname(os.path.realpath(__file__))
        if circuit==1:
            with open('../Circuits/circuit3.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==2:
            with open('../Circuits/circuit4.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==3:
            with open('../Circuits/circuit11.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==4:
            with open('../Circuits/circuit6.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==5:
            with open('../Circuits/circuit1.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==6:
            with open('../Circuits/circuit2.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==7:
            with open('../Circuits/circuit5.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==8:
            with open('../Circuits/circuit7.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==9:
            with open('../Circuits/circuit8.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==10:
            with open('../Circuits/circuit10.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==11:
            with open('../Circuits/circuit9.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)

        if circuit==12:
            with open('../Circuits/circuit12.txt') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)
        if circuit==13:
            with open('../Circuits/circuitTest1.txt') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)

        if circuit==14:
            with open('../Circuits/CircuitTest2.txt') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)

        if circuit==15:
            with open('../Circuits/CircuitTest.csv') as cs:
                entrada = csv.reader(cs)
                x = next(entrada)
                y = next(entrada)
                w = next(entrada)
                self.__points,self.__widths=self.llistes(x,y,w)


    def llistes(self,x,y,w):
        for i in range(len(x)):
            self.__points.append(Point2D(float(x[i]), float(y[i])))
            self.__widths.append(float(w[i]))
        return self.__points,self.__widths




    def points(self):
        return self.__points

    def widths(self):
        return self.__widths


