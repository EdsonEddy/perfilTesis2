#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:23:52 2019

@author: user
"""


def palin(x):
    g=x[::-1]
    if g==x:
        return True
    return False

try:
    
    while True:
        c=0
        n=int(input())
        while n>0:
            pal=input()
            if palin(pal):
                c+=1
            n-=1
        print(c)
        
except EOFError:
    pass

'''
n=int(input())
m=1
res=1
while m<=n:
    res*=m
    if m%2==1:
        print("-"+str(res))
    else:
        print(res)
    m+=1;
'''