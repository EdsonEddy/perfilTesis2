n = int(input())
for i in range(n):
    cad1 = input()
    cad2 = input()
    v1 =[0 for k in range(26)]
    v2 =[0 for k in range(26)]
    for k in range(len(cad1)):
        if cad1[k]!=" ":
            v1[ord(cad1[k])-97] += 1
    for k in range(len(cad2)):
        if cad2[k]!=" ":
            v2[ord(cad2[k])-97] += 1
    ans = 1
    for k in range(26):
         if v1[k]!=v2[k]:
             ans = 0
             break
    if(ans ==1):
         print("Si")
    else:
         print("No")