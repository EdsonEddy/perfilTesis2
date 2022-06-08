from sys import *
n=int(stdin.readline())
for i in range(n):
    cad=str(stdin.readline().split("\n"))
    s=0
    for j in range(len(cad)):
        if(65<=ord(cad[j]) and ord(cad[j])<=90):
            s=s+1
            break
    for j in range(len(cad)):
        if(97<=ord(cad[j]) and ord(cad[j])<=122):
            s=s+1
            break
    for j in range(len(cad)):
        if(48<=ord(cad[j]) and ord(cad[j])<=57):
            s=s+1
            break
    for j in range(len(cad)):
        if(cad[j]=="." or cad[j]=="@" or cad[j]=="-" or cad[j]=="_" or cad[j]==">" or cad[j]=="<"):
            s=s+1
            break
    if(s==4):
        print("Dale no te jackiaran esta vez.")
    else:
        print("No va dar Botas.")
