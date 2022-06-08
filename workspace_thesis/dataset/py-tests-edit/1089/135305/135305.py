import math
n = int(input())
cd = int(math.log(n,10)) + 1
if cd >= 5:
   r = (cd // 2) + 1
   x = n //(10 ** (r - 1))
   e = x % 10
   print(e)
elif cd == 1:
    print(cd)
else:
    print("*")