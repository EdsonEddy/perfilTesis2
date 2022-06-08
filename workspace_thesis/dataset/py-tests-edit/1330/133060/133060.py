l,n=input().split()
l,n=str(l),int(n)
aux=len(l)
ll=l[(aux-n):aux]
l=ll+l[0:(aux-n)]
print(l)