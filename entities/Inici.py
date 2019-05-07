from tkinter import *
from tkinter import messagebox

class Inici:

    def __init__(self):


        self.__ventana = Tk()
        self.__usuari=IntVar(value=1)
        self.__circuit=IntVar(value=1)
        self.__usuari=IntVar(value=1)
        self.__cotxes=IntVar(value=1)
        self.__ponderacion = IntVar(value=1)
        self.__de_facil_a_dificil=IntVar(value=0)
        colorFondo="#000000"
        colorLletra="#FFF"
        self.__ventana.title("Car Machine Learning")
        self.__ventana.geometry("740x700")
        self.__ventana.configure(background=colorFondo)

        Label(self.__ventana,text="Benvingut! Es troba en el Car Machine Learning on els cotxes han entrenat mitjançant l'aprenentatge no supervisat.",
                                     bg=colorFondo, fg=colorLletra).place(x=50, y=10)
        Label(self.__ventana,text="Els cotxes han entrenat en 12 circuits. Els circuits 13,14 i 15 són circuits test.",bg=colorFondo,fg=colorLletra).place(x=50,y=50)

        #self.viaje = Spinbox(self.__ventana, from_=1, to=15, wrap=True,textvariable=self.__circuit)

        #self.viaje.pack(padx=30,pady=80)

        Label(self.__ventana,
              text="Elegeixi un circuit (el valor ha de ser un nombre natural entre 1 i 15):",
              bg=colorFondo, fg=colorLletra).place(x=50, y=70)
        Entry(self.__ventana,textvariable=self.__circuit).place(x=50,y=100)

        Label(self.__ventana,
              text="Vol jugar contra el millor cotxe?",
              bg=colorFondo, fg=colorLletra).place(x=50, y=150)
        Label(self.__ventana,
              text="0 - Si.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=170)
        Label(self.__ventana,
              text="1 - No.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=190)
        Entry(self.__ventana, textvariable=self.__usuari).place(x=50, y=220)
        Label(self.__ventana,
              text="* Si vol, hi haurà dos cotxes en el circuit. Utilitzi les fletxes del teclat per accelerar, frenar i girar.",
              bg=colorFondo, fg=colorLletra).place(x=70, y=250)

        Label(self.__ventana,
              text="* En cas contrari, vol veure el millor cotxe o els 30 cotxes entrenats?",
              bg=colorFondo, fg=colorLletra).place(x=70, y=270)
        Label(self.__ventana,
              text="Introdueixi el número 1 o 30 (en cas d'haver escollit jugar no és necessari emplenar el camp).",
              bg=colorFondo, fg=colorLletra).place(x=70, y=290)
        Entry(self.__ventana, textvariable=self.__cotxes).place(x=70, y=320)

        Label(self.__ventana,
              text="L'entrenament s'ha dut a terme en quatre funcions de ponderació i una quinta basada en un algoritme genètic.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=370)

        Label(self.__ventana,
              text="Introdueixi la ponderació:",
              bg=colorFondo, fg=colorLletra).place(x=50, y=390)

        Label(self.__ventana,
              text="1 - Distància.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=410)

        Label(self.__ventana,
              text="2 - Distància^2.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=430)

        Label(self.__ventana,
              text="3 - Velocitat.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=450)
        Label(self.__ventana,
              text="4 - Velocitat * Distància.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=470)
        Label(self.__ventana,
              text="5 - Distància amb l'algoritme genètic.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=490)

        Entry(self.__ventana, textvariable=self.__ponderacion).place(x=50, y=520)



        Label(self.__ventana,
              text="L'entrenament depèn de l'ordre de la dificultat dels circuits.",
              bg=colorFondo, fg=colorLletra).place(x=50, y=570)

        Label(self.__ventana,
              text="* Si val 0 s'han entrenat de circuits fàcils a circuits difícils [1,2,3,...,12].",
              bg=colorFondo, fg=colorLletra).place(x=50, y=590)
        Label(self.__ventana,
              text="* Si val 1 s'han entrenat de circuits difícils a circuits fàcils [12,11,10,...,1].",
              bg=colorFondo, fg=colorLletra).place(x=50, y=610)
        Label(self.__ventana,
              text="Introdueixi el valor 0 o 1:",
              bg=colorFondo, fg=colorLletra).place(x=50, y=630)

        Entry(self.__ventana, textvariable=self.__de_facil_a_dificil).place(x=50, y=660)



        Button(self.__ventana,text="Comencem!", command=self.start, bg="#000000",fg="white").place(x=560,y=640)

        mainloop()


    def start(self):
        return self.__ventana.quit()




    def circuit(self):
        return self.__circuit.get()

    def usuari(self):
        return self.__usuari.get()

    def ponderacion(self):
        return self.__ponderacion.get()
    def cotxes(self):
        return self.__cotxes.get()
    def de_facil_a_dificil(self):
        return self.__de_facil_a_dificil.get()








#finestra=Inici()
#finestra.start()
#print("hola")

#circuit=finestra.circuit()
#print(circuit)

