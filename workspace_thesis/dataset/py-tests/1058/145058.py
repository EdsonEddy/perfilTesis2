def insort(lista,n):
    for i in range(1, n):
        val = lista[i]
        j = i
        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = val
x=int(input())
for k in range(x):
	n=int(input())
	lista=list(map(int,input().split()))
	insort(lista,n)
	print(*lista)