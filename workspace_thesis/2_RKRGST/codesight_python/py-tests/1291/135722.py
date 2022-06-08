num = input().split()
while num[0] !="" \
           "":
    s = 0
    for i in num:
        s = int(i) + s
    print(s)
    num = input().split()
