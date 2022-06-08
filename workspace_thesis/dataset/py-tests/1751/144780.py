# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:45 2019

@author: Hp
"""

cad=input()
c=0
for i in range(len(cad)):
    if cad[i]=='c':
        c+=1
print(c)