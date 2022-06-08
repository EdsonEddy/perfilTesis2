from sys import stdin
def invierte(n):
    m = 0
    while n > 0:
        d=n%10
        m=m*10+d
        n=n//10
    return m

def palindromo(n):
    m=invierte(n)
    if n==m:
        return True
    else:
        return False
for n in stdin:    
 n=int(n)
 s=0
 while n>0:
     x=int(input())
     if palindromo(x):
         s=s+1
     n=n-1
 print(s)