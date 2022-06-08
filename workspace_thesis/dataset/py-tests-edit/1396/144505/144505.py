# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""

try:
    
    while True:
        a1=input()
        a2=input()
        cad=a1+a2
        alv="abcdefghijklmnopqrstuvwxyz"
        a=set()
        for i in range(len(cad)):
            a.add(cad[i])
        sw=True
        for i in range(len(alv)):
            if not alv[i] in a:
                sw=False
                break
        
        if sw:
            print("Correcto")
        else:
            print("Incorrecto")
        
except EOFError:
    pass


