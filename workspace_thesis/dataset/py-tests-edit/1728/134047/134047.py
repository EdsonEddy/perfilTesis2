import math

n = int(input())

s = 0

while(n>0):
    e = int(math.log10(n))
    a = n //int(pow(10,e))
    n = n% int(pow(10,e))
    if(a%2==0):
        s = (s+a)
print(s)

n = int(input())

s = 0

while(n>0):
    e = int(math.log10(n))
    a = n //int(pow(10,e))
    n = n% int(pow(10,e))
    if(a%2==0):
        s = (s+a)
print(s)
