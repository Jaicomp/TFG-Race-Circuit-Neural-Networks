
import csv

class GuardarCircuit(object):
    def __init__(self,n,guardar):

        if n==1:
            with open('../UsuariCircuits/UsuariCircuit1.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)

        if n==2:
            with open('../UsuariCircuits/UsuariCircuit2.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==3:
            with open('../UsuariCircuits/UsuariCircuit3.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==4:
            with open('../UsuariCircuits/UsuariCircuit4.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==5:
            with open('../UsuariCircuits/UsuariCircuit5.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==6:
            with open('../UsuariCircuits/UsuariCircuit6.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==7:
            with open('../UsuariCircuits/UsuariCircuit7.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==8:
            with open('../UsuariCircuits/UsuariCircuit8Cheste.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==9:
            with open('../UsuariCircuits/UsuariCircuit9Catalunya.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==10:
            with open('../UsuariCircuits/UsuariCircuit10.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)

        if n==11:
            with open('../UsuariCircuits/UsuariCircuit11.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)
        if n==12:
            with open('../UsuariCircuits/UsuariCircuit12.csv', 'w', newline="", encoding='utf-8') as csvfile:
                arxiu = csv.writer(csvfile)
                for dato in guardar:
                    arxiu.writerow(dato)







