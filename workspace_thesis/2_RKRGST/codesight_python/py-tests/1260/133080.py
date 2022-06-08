p=int(input())
g=1
while g<=p:
    g=g+1
    a, b=map(int, input().split(" "))
    if b>a:
        i=b
        while i>0:
            m=a%i
            n=b%i
            i=i-1
            if m==0 and n==0:
                break
        print(i+1)
    else:
        i=a
        while i>0:
            m=a%i
            n=b%i
            i=i-1
            if m==0 and n==0:
                break
        print(i+1)