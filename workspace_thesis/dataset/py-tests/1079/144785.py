# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:45 2019

@author: Hp
"""
def isVowel(f):
    if f=='a' or f=='e' or f=='i' or f=='o' or f=='u':
        return True
    return False

def containsVowel(x):
    for i in range(len(x)):
        if isVowel(x[i]):
            return True
    return False

def VoCs(x):
    for i in range(len(x)-2):
        if ((isVowel(x[i]))and(isVowel(x[i+1]))and(isVowel(x[i+2]))) or ((not isVowel(x[i]))and(not isVowel(x[i+1]))and(not isVowel(x[i+2]))):
            return False
    return True

def Oc(x):
    c=0
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            if (x[i]=='e'and x[i+1]=='e') or (x[i]=='o' and x[i+1]=='o'):
               c+=1 
            else:
                return False
    return True
try:
    while True:
        cad=input()
        if(cad=="end"):
            break
        else:
            if containsVowel(cad) and VoCs(cad) and Oc(cad):
                print("<"+cad+"> is acceptable.")
            else:
                print("<"+cad+"> is not acceptable.")
         
except EOFError:
    pass
