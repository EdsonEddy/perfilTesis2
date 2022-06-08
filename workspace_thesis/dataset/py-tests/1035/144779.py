# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:45 2019

@author: Hp
"""

while True:
    cad=input()
    if cad=="#":
        break
    else:
        res=""
        for i in range(len(cad)):
            if cad[i]==' ':
                res+="%20"
            elif cad[i]=='!':
                res+="%21"
            elif cad[i]=='$':
                res+="%24"
            elif cad[i]=='%':
                res+="%25"
            elif cad[i]=='(':
                res+="%28"
            elif cad[i]==')':
                res+="%29"
            elif cad[i]=='*':
                res+="%2a"
            else:
                res+=cad[i]
        print(res)