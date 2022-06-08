x=int(input())
while x!=0:
    f=0
    s=input()
    n=s.split(" ")
    for i in range(x):
        n[i]=int(n[i])    
    for i in range(x):
        f=f+n[i]
    print(f)        
    x=int(input())
