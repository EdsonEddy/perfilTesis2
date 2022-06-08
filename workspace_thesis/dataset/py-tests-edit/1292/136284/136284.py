def sumar(lista):
    f = int(len(lista))
    sum=0
    for i in range (0,f):
            sum=sum+int(e[i])
    return sum
while True:
    try:
         n=int(input())
         if n == 0:
             break
         e = list(map(str, input().split()))
         f = int(len(e))
         if n == f:
              print(sumar(e))
         else:
             break
    except ValueError:
        break