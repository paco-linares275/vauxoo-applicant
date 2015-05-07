# -*- coding: utf-8 -*-
"""
Receibe a number and check if it is a prime number
"""


class Prime_class:
    """
    This class contains the method to check if the number that is
    entered is a prime number
    """

    def is_prime(self, num_int):
        """
        the name of te method is_prime
        """
        # This indicates the number if times a division led to rest 0
        numero = 0
        # This loop is divided the number that you enter among all the
        # numbers that are between 1 and the number entered
        for valor in range(1, num_int + 1):  # i takes values 1..n
            if num_int % valor == 0:    # if the remainder of the
                # division equal to 0 increases 1
                numero = numero + 1         # The counter is increase
        # If the result contains the counter is different from
        # two then it is not real number so print False and if it
        # does not print
        if numero != 2:
            return False
        else:
            return True

# This variable contains the number is entered if it is a real
# number ignores all number after the decimal point
        num_int = 11
# this class is instantiatd prime_clase and sent to call the method
# is_prime
