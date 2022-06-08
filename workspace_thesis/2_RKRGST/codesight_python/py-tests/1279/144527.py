# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:02:25 2019

@author: Hp
"""
lista=['|','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


try:
    while True:
        R=lambda:map(str,input().split())
        n,cad=R()
        dis=int(n)
        org=""
        for i in range(len(cad)):
            if cad[i]=='_':
                org+=" "
            else:
                org+=cad[i]
        
            
        res=""
        for i in range(len(org)):
            g=-1
            if org[i]>='a' and org[i]<='z':
                for j in range(1,len(lista)):
                    if org[i]==lista[j]:
                        g=j
                        break
                yy=(g+dis)%26
                if yy==0:
                    res+='Z'
                else:
                    for j in range(1,len(lista)):
                        if j==yy:
                            g11=lista[j].upper()
                            res+=g11
            else:
                res+=org[i]
                
        print(res)
         
except EOFError:
    pass