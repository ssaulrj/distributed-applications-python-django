# imports para toda la aplicación
import os
import sys
import random
from types import *
from random import randint, uniform,random

"""def switch_ran(argument):
    switcher = {
        0: 'blanca',
        1: 'roja',
        2: 'azul',
        3: 'verde',
        4: 'amarilla'
    }
    return switcher.get(argument, "Numero random invalido")"""

if __name__ == '__main__':
    while True:
        s = input('Cantidad total de compra: ')
        if int(s) < 100:
            print (':(')
            print ('Cliente no aplica para la promoción, Adios')
            break    
        else:
            print (':)')
            print ('Gasto iguala o supera los $100.00, participa en promoción')

            print ('Color \t\t Descuento')
            print ('Bola blanca \t No tiene')
            print ('Bola roja \t 10% ')
            print ('Bola azul \t 20%')
            print ('Bola verde \t 25%')
            print ('Bola amarilla \t 50%')

            numr = int(random()*4+1)
            print ('Numero: ', numr)
            if numr == 0:
                print ('Felicidades, ha ganado un 0% descuento')
                print ('Su pago seria de: ', (int(s)-int(s)*0))
            elif numr == 1:
                print ('Felicidades, ha ganado un 10% descuento')
                print ('Su pago seria de: ', (int(s)-int(s)*.1))
            elif numr == 2:
                print ('Felicidades, ha ganado un 20% descuento')
                print ('Su pago seria de: ', (int(s)-int(s)*.2))
            elif numr == 3:
                print ('Felicidades, ha ganado un 25% descuento')
                print ('Su pago seria de: ', (int(s)-int(s)*.25))
            elif numr == 4:
                print ('Felicidades, ha ganado un 50% descuento')
                print ('Su pago seria de: ', (int(s)-int(s)*.5))
            print ('')

            ss = input('Si desea salir presione 1 si no otro numero ')   
            if int(ss) == 1:
                print (':(')
                print ('Adios')
                break
