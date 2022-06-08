a, b, c = map( int, input().split())
if a<=b and a<=c:
    print(a, end=" ")
    if b<=c:
        print(b, c, sep=" ")
    else:
        print(c, b, sep=" ")
if b<=a and b<=c:
    print(b, end=" ")
    if a<=c:
        print(a, c, sep=" ")
    else:
        print(c, a, sep=" ")
if c<=a and c<=b:
    print (c, end=" ")
    if a<=b:
        print(a, b, sep=" ")
    else:
        print(b, a, sep=" ")