# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:45 2019

@author: Hp
"""

import itertools
lista=[]
cad1=input()
cad=""
for i in range(len(cad1)):
    if cad1[i]!=' ':
        cad+=cad1[i]
for i in range(len(cad)):
    lista.append(cad[i])
    
list_password=[]
for r in [4,len(cad)]:
    res = itertools.permutations(lista, r)
    for e in res:
        list_password.append(''.join(e))
for i in range(len(list_password)):
    print(list_password[i])
