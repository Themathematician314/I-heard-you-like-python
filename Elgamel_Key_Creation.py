import math
import random
import sys
import os

class Public_Key(object):
    
    def __init__(self, prime=None, g=None, x=None, confidence=None):
        self.__prime = prime
        self.__g = g
        self.__x = x
        self.__confidence = confidence
        
class Private_Key(object):
    
    def __init__(self, prime=None, g=None, x=None, confidence=None):
        self.__prime = prime
        self.__g = g
        self.__x = x
        self.__confidence = confidence
        
def gcd(a, b):
    return math.gcd(a, b)

def power(base, exponent, modulo):
    return ((base**exponent) % modulo)

def Jacobi_Symbol(
