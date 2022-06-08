def masRepetido(x):
    la = max(x)
    ar = la+1
    l = [0]*ar
    for i in x:
        l[i] += 1
    return l.index(max(l))


while True:
    x = int(input())
    y = list(map(int,input().split()))
    va = masRepetido(y)
    c = 0
    for i in range(len(y)):
        if y[i]!= va:
            c +=1
    print(c)