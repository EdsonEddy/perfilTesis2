for i in range(int(input())):
    n=int(input())
    x=n
    nn=0
    while x!=0:
        c=1
        for i in range(x%10):
            c*=i+1
        nn+=c    
        x=x//10
    if n==nn:
        print("Y")
    else:
        print("N")