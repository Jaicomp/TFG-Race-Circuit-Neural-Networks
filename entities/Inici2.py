from tkinter import *

from tkinter import messagebox

class Inici:

    def __init__(self):
        self._windows = Tk()

        self._isCircuit1Enable = IntVar()
        self._isCircuit2Enable = IntVar()
        self._isCircuit3Enable = IntVar()
        self._isCircuit4Enable = IntVar()

        self._windows.title("Simulador del caso de estudio 1.")
        self._windows.geometry("400x70")
        self._windows.resizable(False, False)

        Label(self._windows,
              text="Selecciona el conjunto de circuitos de entrenamiento que quieres utilizar:",
              ).place(x=0, y=0)

        Checkbutton(self._windows,
                    text="Circuito 1",
                    variable=self._isCircuit1Enable
                    ).place(x=0, y=20)

        Checkbutton(self._windows,
                    text="Circuito 2",
                    variable=self._isCircuit2Enable
                    ).place(x=150, y=20)

        Checkbutton(self._windows,
                    text="Circuito 3",
                    variable=self._isCircuit3Enable
                    ).place(x=0, y=40)

        Checkbutton(self._windows,
                    text="Circuito 4",
                    variable=self._isCircuit4Enable
                    ).place(x=150, y=40)

        Listbox(self._windows)

        Button(self._windows,text="Empezar!", command=self.start).place(x=300,y=30)

        mainloop()


    def start(self):
        return self._windows.quit()

    def getCircuitsInBinary(self):
        circuitsInBinary = [
            self._isCircuit1Enable.get(),
            self._isCircuit2Enable.get(),
            self._isCircuit3Enable.get(),
            self._isCircuit4Enable.get()
        ]
        return circuitsInBinary

    def getCircuits(self):
        circuits = []

        if self._isCircuit1Enable.get(): circuits.append(1)
        if self._isCircuit2Enable.get(): circuits.append(2)
        if self._isCircuit3Enable.get(): circuits.append(3)
        if self._isCircuit4Enable.get(): circuits.append(4)

        # More than one circuit is checked or none
        if len(circuits) > 1 or len(circuits) == 0: return None

        return circuits


