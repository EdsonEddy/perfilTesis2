while True:
    cas = int(input())
    nump = input().split()
    la = 0
    if cas == len(nump):
        for i in nump:
            la += int(i)
        print (la)
    else:
        exit()
