def cadena(c):
        #c.replace("aba","",)
        #print(c)
        flag=False
        c=c.replace("\n","")
        x=len(c)
        x=x//2
        c1=c[:x]
        c2=c[len(c)-x:]
        #print(c1,c2)
        a=len(c1)
        b=0
        for i in range(len(c1)-1):
                #print(c1[:a],"\t \t",c2[b:])
                if(str(c1[:a])==str(c2[b:])):
                        flag=True
                        break
                a=a-1
                b=b+1
        #print(c.find("aba"))
        return flag
from sys import stdin
for c in stdin:
        c=str(c)
        if(cadena(c)):
                print("si")
        else:
                print("no")