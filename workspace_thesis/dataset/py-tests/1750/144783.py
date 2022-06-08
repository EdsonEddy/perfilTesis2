# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:45 2019

@author: Hp
"""
def endWith(x, t):
    gr=t[-len(x):]
    if(x==gr):
        return True
    return False

try:
    while True:
        cad=input()
        sw=False
        tg=cad[:2]
        endWith(tg,cad)
        for i in range(len(cad)):
            y=cad[:i]
            if endWith(y,cad):
                print("si")
                sw=True
                break
        if not sw:
            print("no")
         
except EOFError:
    pass
