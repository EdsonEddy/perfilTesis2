while True:
    y = int(input())
    c = 0
    for j in range(y):
        x = input()
        nn = ''
        for i in x:
            nn = i + nn
        if nn == x:
            c+=1
    print(c)