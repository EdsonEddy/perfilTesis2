import math
x = int(input())
x = x*180
aux = math.sin(x)
aux = round(aux,1)+0.1
print(aux)