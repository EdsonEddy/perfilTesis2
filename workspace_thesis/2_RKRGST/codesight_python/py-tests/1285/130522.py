n=int(input())
while n>0:
    x=n
    i=1
    sp=0
    si=0
    while x>0:
        d=x%10
        x=x//10
        if i%2==0:
            sp=sp+d
        else:
            si=si+d
        i=i+1
    if sp==si:
        print("SI")
    else:
        print("NO")
    n=int(input())