# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""
import math
primos=[]
def es_primo(numero):
    for i in range(2,int(math.sqrt( numero ))+1):
        if (numero%i)==0:
            # es divisible
            return False
    return True



try:
    while True:
        n=int(input())
        if es_primo(n):
            print("ES PRIMO")
        else:
            print("NO ES PRIMO")
         
except EOFError:
    pass