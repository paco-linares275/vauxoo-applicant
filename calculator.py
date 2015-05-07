# -*- coding: utf-8 -*-
"""
Calculates the sum of the numbers
"""


class calculator_class:
    """
    This class contains the method that calculates the sum of the
    numbers
    """

    def sum(self, num_list):
        """
        this method calculates the sum of numbers
        """
        # it is instantiated the class calculator_class and sent to
        # call the method sum
        suma = 0  # this variable stores the sum of the numbers
        # This loop realize the sum of the numbers
        for valor in num_list:
            suma += valor
        print suma

        num_list = []  # the numbers are added
        respuesta = 1  # control variable while loop
# In this loop numbers are added to the list called numbers
while respuesta == 1:
    num_list = [2, 4, 5, 6, 7]
    num_list.append(num_list)
    respuesta = ('+'.join(num_list))

calculadora = calculator_class()
calculadora.sum(num_list)
