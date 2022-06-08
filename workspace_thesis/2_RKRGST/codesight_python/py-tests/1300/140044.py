while(True):
    x=int(input())
    c=0
    s=input()
    n=s.split(" ")
    for i in range(x):
        if n[i]==n[x-1]:
            c=c+1
    print(c) 