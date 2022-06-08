import math
sup, n = map(int,input().split())
while sup!=""\
       "":

    c, inf, m = 0,1,0
    while m != n:
        if m < n:
            inf = m + 1
        else:
            sup =m- 1
        m = math.floor((sup + inf) /2)
        c += 1
    print(c)
    sup,n = map(int,input().split())