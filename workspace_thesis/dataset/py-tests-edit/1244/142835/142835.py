import math
n=int(input())
for i in range(n):
    cad = input()
    list = cad.split()
    if list[0] == "circle":
        area = math.pi * (float(list[1]) ** 2)
    else:
        area = float(list[1]) * float(list[2])
    print("{0:.2f}".format(area))