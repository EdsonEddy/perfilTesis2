def recorrerL(c1,c2,l,v1,c):
    for k in range(l):
        v1[ord(c1[k])-97] = k
    ans = 0
    for k in range(1,len(c2)):
        ans += abs(v1[ord(c2[k])-97]-v1[ord(c2[k-1])-97])
    print(ans)


n = int(input())
for i in range(n):
    c1 = input()
    c2 = input()
    v1 = [0 for j in range(26)]
    c = 0
    l = len(c1)
    recorrerL(c1,c2,l,v1,c)