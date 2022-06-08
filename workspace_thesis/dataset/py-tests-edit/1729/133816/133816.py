import math
for k in range(2):
    a=int(input(""))
    b=int(math.log10(a))
    mm=a
    for j in range(b):
        c=pow(10,b)
        n=int(mm/c)
        if n%2==0:
            print(n, end="")
        mm=mm%c
        b=b-1
    n=mm%c
    if n%2==0:
        print (n)
    print("")