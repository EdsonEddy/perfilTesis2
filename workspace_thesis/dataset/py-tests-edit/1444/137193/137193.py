def binarizar(decimal):
    b=bin(decimal)
    g=b[2:]
    return g
casos=int(input())
for i in range(casos):
    n=int(input())
    n2=binarizar(n)
    ocurrencias=n2.count("11")
    print(ocurrencias)