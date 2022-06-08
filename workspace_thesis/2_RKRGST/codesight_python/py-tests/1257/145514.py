n = int(input())
for i in range(n):
    c1 = input()
    c2 = input()
    v1 = [0 for k in range(26)]
    v2 = [0 for k in range(26)]
    for j in range(len(c1)):
        if c1[j]!=" ":
            v1[ord(c1[j])-97]+=1
    for j in range(len(c2)):
        if c2[j]!=" ":
            v2[ord(c2[j])-97]+=1
    ans = 1
    for j in range(26):
        if v1[j]!=v2[j]:
            ans = 0
            break
    if ans==1:
               print("Si")
    else:
               print("No")
