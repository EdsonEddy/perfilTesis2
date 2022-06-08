n=int(input())
l=''
m=' '
l=input().split(' ')
m=l[::-1]
if l==m:
    print('SI')
else:
    print('NO')