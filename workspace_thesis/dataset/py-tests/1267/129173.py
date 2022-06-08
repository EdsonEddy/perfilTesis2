n=int(input())
if 0 <= n <= 1000:
    r = (n * 2) + 1
    print(r)
    for i in range(n):
        x=int(input())
        if not x == -1:
            if x == 1:
                r = 3
            else:
                r = (x*2)+1
            print(r)
        else:
            break
else:
    print("reset!")