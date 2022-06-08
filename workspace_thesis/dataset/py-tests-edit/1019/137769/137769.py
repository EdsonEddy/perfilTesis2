t=int(input())
if t<=20:
    for k in range(1,t+1):
        a, b, c=map(int, input().split())
        if a<=b:
            if b<=c:
                print("Case", k, sep=" ", end="")
                print(":", b, sep=" ")
            else:
                if a<=c:
                    print("Case", k, sep=" ", end="")
                    print(":", c, sep=" ")
                else: 
                    print("Case", k, sep=" ", end="")
                    print(":", a, sep=" ")
        else:
            if a<=c:
                print("Case", k, sep=" ", end="")
                print(":", a, sep=" ")
            else:
                if b<=c:
                    print("Case", k, sep=" ", end="")
                    print(":", c, sep=" ")
                else: 
                    print("Case", k, sep=" ", end="")
                    print(":", b, sep=" ")
    