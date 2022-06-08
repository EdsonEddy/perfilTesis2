def criba(v,f):
    v[0] = False
    v[1] = False

    for i in range (2,f-1):
        if v[i]:
            for j in range(i+i,f-1,i):
                v[j] = False    


f = 1000000
v = [True]*f
criba(v,f)
while True:
    n = int(input())
    if v[n]:
        print("SI")
    else:
        print("NO")