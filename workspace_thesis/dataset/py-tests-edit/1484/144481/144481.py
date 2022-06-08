import math


def prim(n):
    if n < 2:
        return False
    for i in range(2,(int(math.sqrt(n)+1))):
        if n % i == 0:
            return False
    return  True


n = int(input())
cx = 1
su = 0
pr = 1
for i in range(1,n+1):
    su = su + cx
    cx+=1
    while not prim(pr):
        pr += 1
    if i % 2 ==0:
        print(str(pr)+'/'+str(su))
    else:
        print(str(su) + '/' + str(pr))
    pr += 1