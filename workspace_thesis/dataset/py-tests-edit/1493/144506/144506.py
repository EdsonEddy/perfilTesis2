# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""

t=input()
s=input()
t=t.lower()
s=s.lower()
for i in range(len(t)-1):
    k=t[:len(s)]
    if k==s:
        print(i)
    t=t[1:]
   


