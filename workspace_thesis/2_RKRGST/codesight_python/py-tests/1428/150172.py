import math
x1, y1, x2, y2 = list(map(float, input().split()))
print("%.2f" % math.sqrt((x1-x2)**2+(y1-y2)**2))