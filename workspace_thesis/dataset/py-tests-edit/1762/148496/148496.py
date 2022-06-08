import collections
while True:
    try:
        n=int(input())
        c=0
        if 1 <= n and n <=100:
            l=[int(e) for e in input().split()]
            s=collections.Counter(l)
            for e in range(1,101):
              if s[e]!=0:
                  p=s[e]//2
                  c=c+p
            print(c)
    except ValueError:
        break