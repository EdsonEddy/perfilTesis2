import sys
def f(n):
   ans = n
   while n:
      ans += n%10
      n //= 10
   return ans
N = 10002
A = [1]*N
v = [0]
for i in range(1,N):
   a = f(i)
   if A[i]:
      while a<N-1:
         A[a] = 0
         a = f(a)
for i in range(1,N):
   v.append(v[i-1]+A[i])
if __name__=='__main__':
    for x in sys.stdin:
   		a, b = map(int, x.split())
   		print(v[b]-v[a-1])