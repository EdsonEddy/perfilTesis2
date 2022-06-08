while True:
    n=int(input())
    x=1
    c=1
    for i in range(n,0,-1):
        print("-"*i+str(x)*c+"-"*i)
        x+=1
        c+=2
