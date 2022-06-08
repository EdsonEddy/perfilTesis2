n = int(input())
cont,i=1,1
while cont<=n:
    if i <= n :
        print(cont,end="/")
        print(i)
        i = i + 1
    else:
        cont = cont + 1
        i = 1