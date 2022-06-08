import sys
def leeV(x):
    global A
    A = x.split(" ")
def comp(A, n):
    y = 0
    i = 0
    while i<n:
        if A[i] == A[n-1]:
            y = y + 1
        i = i+1
    return y


A = []
for n in sys.stdin:
    n = int(n)
    w = input()
    leeV(w)
    y = comp(A, n)
    print(y)