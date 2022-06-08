def inv(x):
    if x[::-1]==x:
        return 1
    return -1

n=int(input())
while n!="" \
         "":
    c = 0
    for i in range(n):
        x = input()
        if inv(x) == 1:
            c += 1
    print(c)
    n = int(input())
