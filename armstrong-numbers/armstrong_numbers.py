from math import log10

def is_armstrong(number):
    origin = number
    while number is not 0:
        origin -= pow(number % 10, int(log10(origin))+1)
        number = int(number / 10)
    if origin is 0:
        return True
    return False
