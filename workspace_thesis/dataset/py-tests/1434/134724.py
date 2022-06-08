x=int(input())
a=x
r=0
while x>0:
    d=(x%10)
    r=r*10+d
    x=x//10
if a==r:
    print("S")
else:
    print("N")