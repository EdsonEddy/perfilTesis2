import sys
def primo(n):
    cd = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            cd = 0
        d = d + 1
    if cd == 1:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
for n in sys.stdin:
    n = int(n)
    primo(n)