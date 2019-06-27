from tkinter import *
from tkinter import messagebox

class Inici:

    def __init__(self):
        self._windows = Tk()

        self._isCircuit1Enable = IntVar()
        self._isCircuit2Enable = IntVar()
        self._isCircuit3Enable = IntVar()
        self._isCircuit4Enable = IntVar()
        self._isCircuit5Enable = IntVar()
        self._isCircuit6Enable = IntVar()
        self._isCircuit7Enable = IntVar()

        self._windows.title("Visualization test case")
        self._windows.geometry("550x300")
        self._windows.resizable(False, False)

        Label(self._windows,
              text="Selecciona el conjunto de circuitos de entrenamiento que quieres utilizar para el caso de prueba:",
              ).place(x=0, y=0)

        Checkbutton(self._windows,
                    text="Circuito 1",
                    variable=self._isCircuit1Enable
                    ).place(x=0, y=20)

        Checkbutton(self._windows,
                    text="Circuito 2",
                    variable=self._isCircuit2Enable
                    ).place(x=0, y=50)

        Checkbutton(self._windows,
                    text="Circuito 3",
                    variable=self._isCircuit3Enable
                    ).place(x=0, y=80)

        Checkbutton(self._windows,
                    text="Circuito 4",
                    variable=self._isCircuit4Enable
                    ).place(x=0, y=110)

        Checkbutton(self._windows,
                    text="Circuito 5",
                    variable=self._isCircuit5Enable
                    ).place(x=0, y=140)

        Checkbutton(self._windows,
                    text="Circuito 6",
                    variable=self._isCircuit6Enable
                    ).place(x=0, y=170)

        Checkbutton(self._windows,
                    text="Circuito 7",
                    variable=self._isCircuit7Enable
                    ).place(x=0, y=200)


        Button(self._windows,text="Empezar!", command=self.start).place(x=10,y=230)

        mainloop()


    def start(self):
        return self._windows.quit()

    def getCircuitsInBinary(self):
        circuitsInBinary = [
            self._isCircuit1Enable.get(),
            self._isCircuit2Enable.get(),
            self._isCircuit3Enable.get(),
            self._isCircuit4Enable.get(),
            self._isCircuit5Enable.get(),
            self._isCircuit6Enable.get(),
            self._isCircuit7Enable.get()
        ]
        return circuitsInBinary

    def getCircuits(self):
        circuits = []

        if self._isCircuit1Enable.get(): circuits.append(1)
        if self._isCircuit2Enable.get(): circuits.append(2)
        if self._isCircuit3Enable.get(): circuits.append(3)
        if self._isCircuit4Enable.get(): circuits.append(4)
        if self._isCircuit5Enable.get(): circuits.append(5)
        if self._isCircuit6Enable.get(): circuits.append(6)
        if self._isCircuit7Enable.get(): circuits.append(7)

        return circuits

