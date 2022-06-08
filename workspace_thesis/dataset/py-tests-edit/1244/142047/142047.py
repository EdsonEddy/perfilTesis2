import math
def circle(to):
    di = math.pi
    are = n*n*di
    to = print('{0:.2f}'.format(are))
    return to
while True:
    c = int(input())
    for x in range(c):
        d = input()
        if d[0:6] == "circle":
            n = d[7:len(d)]
            n = int(n)
            circle(n)
        elif d[0:9] == "rectangle":
            d = d.split()
            h = float(d[1])
            b = float(d[2])
            ar = h*b
            print('{0:.2f}'.format(ar))
