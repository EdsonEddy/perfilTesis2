import sys
def palindromo(x):
    a=x
    s=0
    while (x>0):
        d=x%10
        x=x//10
        s=s*10+d
    if a==s:
        return 1
    else:
        return 0
  

for x in sys.stdin:
    n=int(x)
    c=0
    for i in range (n):
        y=int(input())
        if palindromo(y):
            c=c+1
    print (c)