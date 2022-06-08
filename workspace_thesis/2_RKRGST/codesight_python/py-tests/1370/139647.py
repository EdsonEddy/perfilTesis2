while True:
    n=int(input())
    b=bin(n)
    c=b.split("b")
    final=len(c[1])
    print(final)