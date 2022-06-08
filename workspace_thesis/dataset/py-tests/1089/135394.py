import math
n=int(input())
c=int(math.log10(n)) + 1
x = n
if c % 2 == 0:
    print("*")
else:
    
    while n > 0:
        a=n%10
        
        d=int(x/10**(c-1))
        x = x%10**(c-1)
        c = c-1
        
        
        if a == d:
            
            break
        n=int(n/10)    

print(a)
