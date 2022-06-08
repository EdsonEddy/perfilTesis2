n=int(input())
for q in range(n):
    c=int(input())
    A=list(map(int,input().split()))
    B=sorted(A)
    str1=' '.join(str(e)for e in B)
    print(str1)


