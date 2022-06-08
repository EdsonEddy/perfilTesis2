def sol (n):
    l=["2","4","8","7","5","1"]
    r=n%6
    return l[r]

while True:
    n=int(input())
    for i in range(n):
        s=int(input())
        print(sol(s))