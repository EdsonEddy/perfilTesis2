while True:
    x=input()
    if x=="fin":
        break
    y=int(x)
    s=0
    for i in range (y):
        n=int(input())
        s=s+n
    print(s)
