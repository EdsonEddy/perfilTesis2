import math
n = (input())
x = ''
for i in n:
    x = i + x
if x == n:
    print('S')
else:
    print('N')