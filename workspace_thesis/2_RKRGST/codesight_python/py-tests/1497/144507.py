# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""




r=input()
res=""
for i in range(len(r)):
    if (r[i]>='A' and r[i]<='Z')or(r[i]>='a' and r[i]<='z')or(r[i]>='0' and r[i]<='9'):
        l=ord(r[i])
        ll=int(bin(l)[2:])
        g=str(ll)
        if(not len(g)==8):
            hh=""
            for i in range(8-len(g)):
                hh+="0"
            g=hh+g
        
        res+=g
    elif r[i]==' ':
        res+="00100000"
print(res)
