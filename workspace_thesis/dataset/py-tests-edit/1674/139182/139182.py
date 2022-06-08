def f(n):
    return (n*(n+1)/2)-(n-1)
if __name__=='__main__':    
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        print(str(int(f(n))))