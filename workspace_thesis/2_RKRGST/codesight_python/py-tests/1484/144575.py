# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""
lista1=[]
primos=[]
def es_primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True

def l1():
    o=2
    k=1
    for i in range(2001):
        lista1.append(k)
        k=k+o
        o+=1

def l2():
    c=0
    con=2
    while True:
        if(c==2000):
            break
        else:
            if es_primo(con):
                primos.append(con)
                c+=1
        con+=1

l1()
l2()
n=int(input())
for i in range(n):
    if i%2==0:
        print(str(lista1[i])+"/"+str(primos[i]))
    else:
        print(str(primos[i])+"/"+str(lista1[i]))