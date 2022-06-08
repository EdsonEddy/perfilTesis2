def contarletras(cad):
    c = 0
    m = len(cad)
    for i in range(0, m, 1):
        a = ord(cad[i])
        if(65 <= a and a <= 90):
            c = c + 1
    return c

n = int(input())
flag = 0
for i in range(n):
    x = input()
    y = input()
    x = x.upper()
    y = y.upper()
    a = contarletras(x)
    b = contarletras(y)
    if a == b:
        for i in range(0, len(x)):
            c = x[i]
            for j in range(0,len(y)):
                if (c == y[j] and c != chr(32) ):
                    flag = flag + 1
                    
                    break
    

    if flag == a:
        print("Si")
    else:
        print("No")

    flag = 0
