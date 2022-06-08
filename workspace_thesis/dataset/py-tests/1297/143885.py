def inv(a):
    return a[::-1]
n= int(input())
for i in range(n):
    texto=input()
    x=inv(texto)
    print(x)
