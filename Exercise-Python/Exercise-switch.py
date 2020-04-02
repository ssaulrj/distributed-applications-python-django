# imports para toda la aplicación
import os
import sys
import random
from types import *
from random import randint, uniform,random

def switch_precios(argument):
    switcher = {
        1: '10',
        2: '20',
        3: '30',
        4: '40',
        5: '50',
        6: '60',
        7: '70',
        8: '80',
        9: '90',
       10: '100'
    }
    return switcher.get(argument, "Numero random invalido")

if __name__ == '__main__':
    while True:
        print ('Elige producto deseado')
        print (' ')    
        print ('\tProducto   \t Codigo')
        print (' ')
        print ('\tCamisa     \t 1')
        print ('\tCinturon   \t 2')
        print ('\tZapatos    \t 3')
        print ('\tPantalon   \t 4')
        print ('\tCalcetines \t 5')
        print ('\tFaldas     \t 6')
        print ('\tGorras     \t 7')
        print ('\tSueter     \t 8')
        print ('\tCorbata    \t 9')
        print ('\tChaqueta   \t 10')
        print (' ')
        
        c = input('Introduzca codigo: ')
        pc = switch_precios(int(c))
        print ('Precio de producto: ',pc)
        nu = input('Introduzca numero de unidades: ')

        print (' ')
        print ('Total a pagar es ', (int(pc)*int(nu)) )
        print (' ')
        
        ss = input('Si desea salir presione 1 si no otro numero ')   
        if int(ss) == 1:
           print (':(')
           print ('Adios')
           break
