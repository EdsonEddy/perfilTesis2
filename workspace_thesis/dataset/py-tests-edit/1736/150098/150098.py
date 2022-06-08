n=int(input())
c=0
cad=""
while n>0 :
    n=n-1;
    s=(2**(2**c))+1
    cad=cad+str(s)+" "
    c=c+1;
m=len(cad)
cadd=cad[0:(m-1)]
print(cadd)