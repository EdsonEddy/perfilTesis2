cad,n=map(str,input().split())
t=int(n)
s=0
#print("ssss",s)
a=cad[len(cad)-t:]
#print("aaa",a)
b=cad[:len(cad)-t]
#print("bbb",b)
print (a+b)