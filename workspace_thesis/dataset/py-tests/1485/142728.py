n=0
while n!="":
    n=int(input())
    k=0
    for i in range(n):
        s=str(input())
        if s[::-1]==s:
            k=k+1
    print(k)