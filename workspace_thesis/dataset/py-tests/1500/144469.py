a=int(input())
l=list(map(int,input().split()))
if l==l[::-1]:
    print('SI')
else:
    print('NO')
