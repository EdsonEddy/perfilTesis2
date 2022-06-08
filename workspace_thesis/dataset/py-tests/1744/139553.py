
n = int(input())
if n % 2 == 0:
    ld = []
    li = []
    for k in range(1, n + 1):
        li.append(k)
    for j in range(n - 1, 0, -1):
        ld.append(j)
    li.extend(ld)
    ck = 0
    for i in range(n):
        for h in li:
            print(h, end="")
        ind = len(li) // ck
        li[ind + ck] = " "
        ck += 1
        li[-(ind + ck)] = " "
        print()

else:
    ld = []
    li = []
    for k in range(1,n+1):
        li.append(k)
    for j in range(n-1,0,-1):
        ld.append(j)
    li.extend(ld)
    ck = 2
    for i in range(n):
        for h in li:
            print(h,end = "")
        ind = len(li) // ck
        li[ind] = " "
        li[-(ind+1)] = " "
        ck += 1
        print()