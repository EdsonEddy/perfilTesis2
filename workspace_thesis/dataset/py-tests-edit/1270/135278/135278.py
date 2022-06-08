from sys import stdin
for x in stdin:
    x = int(x)
    for n in range(x):
        n = int(input())
        if(n == 0):
            print(1)
            continue
        if(n == 1):
            print(0)
            continue
        if(n % 2 != 0):
            print(4, end = "")
        n-=1
        while(n > 0):
            print(8, end = "")
            n-=2
        print()
