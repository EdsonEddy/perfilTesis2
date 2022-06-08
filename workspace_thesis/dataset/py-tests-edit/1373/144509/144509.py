# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""




n=input()
if n==n.lower():
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        print("minuscula")
        print("vocal")
    else:
        print("minuscula")
        print("consonante")
elif n==n.upper():
    if n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U':
        print("mayuscula")
        print("vocal")
    else:
        print("mayuscula")
        print("consonante")
    