# -*- coding: utf-8 -*-
# Este programa recibe una lista de numeros y calcula la suma de los mismos
# Clase que contiene el metodo que calcula la suma de los numeros
class calculator_class:
# Este metodo calcula la suma de los numeros
    def sum(self):
        # Se instancia la clase calculator_class y se manda a llamar
        # el metodo sum
        numeros = []  # Se agregan los numeros
        suma = 0  # En esta varable se lmacena la suma de los numeros
        respuesta = 1  # Esta es la variable de control del ciclo while
        #En este ciclo se agregan los numeros en la lista llamada numeros
        while(respuesta == 1):
            num = (int(input("Ingresar un numero ")))
            numeros.append(num)
            respuesta = (input("Agregaras mas numeros? 1=si 2=no "))
 # Este ciclo realiza la suma de los numeros
        for i in numeros:
            suma += i
        print(suma)
calculadora = calculator_class()
calculadora.sum()
