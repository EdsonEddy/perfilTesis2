while True:
    li=input().split()
    r=0
    R=0
    for i in range(len(li)):
        r=int(li[i])+r
    print(r)