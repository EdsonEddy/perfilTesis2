n = int(input())
for i in range(1, n+1):
    x, y = map(int, input().split(" "))
    if x > y:
        print(">")
    elif x<y:
        print("<")
    else:
        print("=")