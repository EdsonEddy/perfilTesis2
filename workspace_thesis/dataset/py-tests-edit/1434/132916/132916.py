n = int(input())
aux=n
nn=0
while n>0:
    nn=nn*10+n%10
    n=n//10
if nn==aux:
    print("S")
else:
    print("N")