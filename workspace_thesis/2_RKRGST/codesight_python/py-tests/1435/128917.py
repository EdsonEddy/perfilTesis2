n, k = map(int,input().split())
d = 0
s = 0
NUM = 0
while(n != 0):
       d = n % 10
       n = n // 10
       NUM = NUM * 10 + d
       s = s + 1
i = 1
while(i <= k):
       dd = NUM % 10
       NUM = NUM // 10
       i = i + 1
print(s,dd)