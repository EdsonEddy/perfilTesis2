def cantidad(x):
    ce=len(x)
    i=0
    c=0
    while(i<ce):
        if(x[i]=="c" or x[i]=="C"):
            c=c+1
        i=i+1
    return c    
x=input()
ca=cantidad(x)
print (ca)
