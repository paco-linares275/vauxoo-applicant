# -*- coding: utf-8 -*-
# Recibe un numero y verifica si es un numero primo


# Esta clase contiene el metodo para verificar si el numero que se ingresa
# es un numero primo
class prime_class:

    def is_prime(self):  # El nombre del metodo is_prime

# Esta variable contiene el numero que se ingresa, en caso que sea un numero
# real ignora todos los numeros despues del punto decimal
        numero = int(input("Ingresar numero entero"))
        # Esto indica el numero de veces que una division dio como resto 0
        n = 0
        # En este ciclo se divide el numero que se ingresa entre todos los
        # numeros que se ecuentran entre 1 y el numero ingresado
        for i in range(1, numero + 1):  # i toma los valores de 1..n
            if(numero % i == 0):  # Si el residuo de la division es
                                #igual a 0 n aumenta 1
                n = n + 1         # Aqui el contador aunmenta

        # Si el resultado que contiene el contador es diferente a dos,
        #entonces no es un numero real, por lo que imprime False, y
        #si no es así imprime true
        if (n != 2):
            print (False)
        else:
            print (True)

# Se instancia la clase prime_class y se manda a llamar el metodo is_prime
primo = prime_class()
primo.is_prime()
