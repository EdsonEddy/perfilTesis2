def f(_n):
    _f=1
    for i in range(1,_n+1):
            _f*=i
    return _f        
    
for i in range(int(input())):
    n=int(input())
    x=n
    nn=0
    while x!=0:
        nn+=f(x%10)
        x=x//10
    if n==nn:
        print("Y")
    else:
        print("N")