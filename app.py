import funciones as fun
import random
from os import system
system('cls')
lista=[]
id = 0
while True:
    opc =  input('''
1.	Registrar consumo
2.	Listar los todos los consumos
3.	Imprimir hoja consumo
4.	Buscar un consumo por ID
5.	Salir del programa

''')
    
    if opc == '1':
        fun.registar(lista,id)
        id += 1
    elif opc == '2':
        fun.listar(lista,id)
    elif opc == '3':
        fun.imprimir(lista)
    elif opc =='4':
        print()
    elif opc == '5':
        break
