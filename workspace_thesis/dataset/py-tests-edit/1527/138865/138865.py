c=int(input())
s=0

for i in range(c):
    n=int(input())
    while n!=0:
        d=n%100
        n=n//10
        if d==96:
            s=s+1
            
    if s>=1:
        print("APLAZADO!")    
    else:
        print("TE SALVAS :D")          
    s=0
          