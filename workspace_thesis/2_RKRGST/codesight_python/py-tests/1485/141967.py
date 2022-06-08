def pal(n):
    s=n[::-1]
    if n==s:
        return True
    else:
        return False

from sys import stdin
for i in stdin:
    x=int(i)
    s=0
    for j in range(x):
        
        n=str(int(input()))
        if pal(n):
            s=s+1
    print(s)