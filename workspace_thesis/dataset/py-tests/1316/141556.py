def ordenar_min(b):
    for x in range(len(b)):
        for m in range(len(b)):
            if b[x] < b[m]:
                tmp = b[m]
                b[m] = b[x]
                b[x] = tmp

    
def ordenar_max(a):
    for xd in range(len(a)):
        for m in range(len(a)):
            if a[xd] > a[m]:
                tmp = a[xd]
                a[xd] = a[m]
                a[m] = tmp

def multi(a,b):
    n = 0
    n1 = 0
    for i in range(len(a)):
        n1 = a[i]*b[i]
        n = n1 + n
    print(n)
while True:
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    ordenar_min(a)
    ordenar_max(b)
    multi(a, b)

