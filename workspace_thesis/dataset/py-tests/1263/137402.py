import math
while True:
    sup, cho = map(int,input().split())
    inf = 1
    c = 0
    x = 1
    while x != cho:
        x = math.floor((sup + inf)/2)
        if x < cho:
            inf = x + 1
        elif x > cho:
            sup = x - 1
        c+=1
    print(c)