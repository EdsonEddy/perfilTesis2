import math
x = int(input())
for i in range(x):
    n, k =map(int,input().split())
    pr = k * ((n)*(n+1)//(2))
    print(pr)