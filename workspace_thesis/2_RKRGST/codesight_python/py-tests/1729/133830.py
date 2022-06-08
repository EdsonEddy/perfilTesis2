import math

n = int(input())
            
while(n>0):
    e = int(math.log10(n))
    a = n //int(pow(10,e))
    n = n% int(pow(10,e))
    if(a%2==0):
        print(str(a),end='')
print()
n = int(input())
            
while(n>0):
    e = int(math.log10(n))
    a = n //int(pow(10,e))
    n = n% int(pow(10,e))
    if(a%2==0):
        print(str(a),end='')
print()