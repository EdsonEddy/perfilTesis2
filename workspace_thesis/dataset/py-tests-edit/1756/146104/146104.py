n = int (input())
for n in range (n):
    x = int ( input())
    x = x % 6
    a = 2
    for i in range(x):
        a = a * 2
        if len(str(a)) != 1:
            c = 0
            j = 0
            for j in str(a) :
                c = c + int(j)
            a = c
    print(a)

