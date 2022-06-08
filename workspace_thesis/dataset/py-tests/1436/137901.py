from itertools import permutations
import math
a,b,c = map(int, input().split(" "))
x = [a, b, c]
p = permutations(x)
res = 0
for i in list(p):
    cad = ""
    for j in range(len(i)):
        cad = cad + str(i[j])
    res = max(res, int(cad))
print(res)
