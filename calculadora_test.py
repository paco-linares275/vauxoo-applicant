# -*- coding: utf-8 -*-

# Aqui importamos la clase calculator_class
from calculator import calculator_class


# Esta clase calculator_test hereda lo que contiene en la
# clase calculator_class
class calculator_test(calculator_class):

    def calculator(self):  # Este metodo captura los numeros que se ingresaron

        # Esta variable indica la cantidad de numeros que el
        # usuario va ingresar
        centinela = int(input("Escriba la cantidad de numeros que ingresara "))
        numeros = []  # Es la lista donde se almacenan los numeros 
        # que se ingresaron
        contador = 0  # Es la variable de control para llenar 
        # la lista de numeros
        # Este ciclo es para insertar los numeros ingresados en la 
        # lista numeros
        while (contador <= centinela - 1):
            number = input("Ingresar un numero ")
            numeros.append(number)
            contador = contador + 1
        suma = calculator_class()  # Se instancia de la clase calculator_class
        suma.sum(numeros)  # Llamamos al metodo sum que suma todos los numeros
calculadora = calculator_test()  # Se instancia de la clase calculator_test
calculadora.calculator()  # Llamamos al metodo que recibe los numeros 
                            # que se ingresan
  
  
    #Haber si me exlico...  
    # Para que funcione este programa llamado calculator_test tuve que
    # modificar el codigo del programa anterior para que funcionara en 
    # difeenctes modulos solo que este modificado solo recibe una lista 
    # de numeros y realiza la suma y así funciona el programa calculator_test

    # Y aquí esta el codigo del programa llamado calculator.py 
    # pero modificado para que funcionara el programa calculator_test


    # -*- coding: utf-8 -*-


# Esta clase contiene el metodo que calcula la suma de los numeros
class calculator_class:
# Este metodo calcula la suma de los numeros
    def sum(self, numeros):
        # Se instancia la clase calculator_class y se manda a llamar
        # el metodo sum
        suma = 0  # En esta varable se almacena la suma de los numeros
 # Este ciclo realiza la suma de los numeros
        for i in numeros:
            suma += i
        print(suma)
        
