# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""




r=input()
res=""

while len(r)>0:
    k=r[:8]
    rr=int(str(k), 2)
    nn=chr(rr)
    res+=nn;
    r=r[8:]
print(res)
