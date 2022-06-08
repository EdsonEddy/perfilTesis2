from sys import stdin,stdout
t,out = map(str,stdin.readline().split('\n'))
t = int(t)
for i in range(t):
    s,out = map(str, stdin.readline().split('\n'))
    q,out = map(str, stdin.readline().split('\n'))
    v = [0 for i in range(260)]
    for j in range(len(s)):
        if s[j]==' ':
            continue
        v[ord(s[j])]+=1
    for j in range(len(q)):
        if q[j]==' ':
            continue
        v[ord(q[j])]-=1
    flag = True
    for j in range(len(v)):
        if v[j]!=0:
            flag = False
            break
    if flag:
        stdout.write('Si\n')
    else:
        stdout.write('No\n')