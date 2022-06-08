#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:23:52 2019

@author: user
"""
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