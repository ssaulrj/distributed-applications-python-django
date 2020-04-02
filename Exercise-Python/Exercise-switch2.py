# imports para toda la aplicación
import os
import sys
import random
from types import *
from random import randint, uniform,random

def switch_precios(argument):
    switcher = {
        1: '2.50',
        2: '3.00',
        3: '3.50',
        4: '4.00',
        5: '0.50',
        6: '0.75',
        7: '1.00',
        8: '1.50'
    }
    return switcher.get(argument, "Numero random invalido")

if __name__ == '__main__':
    while True:
        print (' ')    
        print ('     Categoría  \tPrecio  \tCodigo  \tRecargo/d. atraso')
        print (' ')
        print ('\tFavoritos     \t$2.50   \t1       \t$0.50')
        print ('\tNuevos        \t$3.00   \t2       \t$0.75')
        print ('\tEstrenos      \t$3.50   \t3       \t$1.00')
        print ('\tSuper estrenos\t$4.00   \t4       \t$1.50')
        print (' ')
        
        c = input('Codigo categoria de pelicula: ')
        pc = switch_precios(int(c))
        pr = switch_precios(int(c)+4)
        nu = input('Numero de dias de atraso en devolucion: ')

        print (' ')
        print ('Total a pagar es $', (float(pr)*float(nu)+float(pc)),' pesos' )
        print (' ')
        
        ss = input('Si desea salir presione 1 si no otro numero ')   
        if int(ss) == 1:
           print (':(')
           print ('Adios')
           break
