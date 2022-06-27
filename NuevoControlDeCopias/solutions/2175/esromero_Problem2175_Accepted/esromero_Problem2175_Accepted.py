import sys
n=int(sys.stdin.readline())
for i in range(n):
    m=int(sys.stdin.readline().strip())
    a = 1
    b = 0
    c = 0
    for q in range(50):
        c = b
        b = a + b
        a = c
        if m==c:
            print(q)
            break
