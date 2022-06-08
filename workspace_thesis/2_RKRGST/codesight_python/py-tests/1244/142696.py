import math
casos=int(input())
for i in range(casos):
    s=list(input().split(" "))
    if s[0]=="circle":
        r=float(s[1])*math.pi*float(s[1])
        print("{:.02f}".format(r))
    elif s[0]=="rectangle":
        b=float(s[1])
        h=float(s[2])
        area=h*b
        print("{:.02f}".format(area))