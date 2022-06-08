#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:23:52 2019

@author: user
"""
lpares=[]
lfibo=[]

def pares():
    for i in range(2,1002,2):
        lpares.append(i)
        
def fibo():
    a=1
    b=0
    for i in range(1000):
        c=a+b
        lfibo.append(c)
        a=b
        b=c


try:
    pares()
    fibo()
    while True:
        n=int(input())
        c=0
        c2=0
        for i in range(n):
            if i%2==0:
                print(lfibo[c2])
                c2+=1
            else:
                print(lpares[c])
                c+=1
        
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