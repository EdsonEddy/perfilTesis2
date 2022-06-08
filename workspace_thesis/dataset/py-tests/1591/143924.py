#a=1227
#a=1111
def f(a):
    return list(map(int, str(a)))

primos=[2,3,5,7]
g=-1
#print(z)
def operaciones(z):
    ls = []
    for i in z:
        if i in primos:
            ls.append(i)
    if ls == []:
        print(g,end="")
    print(''.join(map(str, ls)))

n=int(input())
while n>0:
    a=int(input())
    z=f(a)#esto es una lista ojo
    operaciones(z)
    n-=1