#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:23:52 2019

@author: user
"""


def isPrime(n):
    for i in range(2,n):
        if (n%i)==0:
            return False
    return True

try:
    while True:
        cad=input()
        r=input()
        for i in range(len(cad)):
            g=cad[i]
            if r==g:
                print(i)
        
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