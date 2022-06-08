n = int(input())
c = input()
c = c.split(' ')
f = []
for i in range(n):
    f.append(int(c[i]))
    s = True
for i in range(int(n/2+1)):
    if f[i]!=f[n-i-1]:
        s = False
        break
if s:
    print('SI')
else:
    print('NO')