import sys
def f(n):
    v = (1,1,2,6,24,120,720,720*8,720*8*9,0)
    c = 0
    while n:
        c += v[n%10]
        n = n//10
    return c
if __name__=='__main__':
    for x in sys.stdin:
        t = int(x)
        while t:
            t -= 1
            n = int(input())
            if n==f(n):print('Y')
            else: print('N')