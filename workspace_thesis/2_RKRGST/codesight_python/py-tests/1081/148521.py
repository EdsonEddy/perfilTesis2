def criba(n):
    r = int(n**0.5)+1
    for i in range(2,r):
        if p[i]==0:
            for j in range(i+i,n,i):
                p[j]=1


n = 1000000
p = [0]*n
criba(n)
# print(p)
casos = int(input())
for i in range(casos):
    pos = int(input())
    if pos == 0 or pos == 1:
        pass
    else:
        cd = pos
        ci = pos
        while p[cd] != 0:
            cd += 1
            # print(cd,'cd')
        while p[ci] != 0:
            ci -= 1
            # print(ci,'ci')
        # print(cd, ci, 'cd ci')
        cd -= pos
        ci = pos - ci
        # print(cd,ci,'cd ci')
        print(cd if cd < ci else ci)
