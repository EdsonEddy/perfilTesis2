n, k = map(int,input().split())
d = 0
s = 0
num = 0
while(n != 0):
       d = n % 10
       n = n // 10
       num = num * 10 + d
       s = s + 1
i = 1
while(i <= k):
       dd = num % 10
       num = num // 10
       i = i + 1
print(s,dd)