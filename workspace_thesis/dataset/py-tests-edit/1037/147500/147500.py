n=int(input())
for i in range(n):
    cad1=input()
    cad2=input()
    v1=[0 for k in range(26)]
    c=0
    for k in range(len(cad1)):
        v1[ord(cad1[k])-97] = k
    ans=0
    for k in range(1,len(cad2)):
        ans+=abs(v1[ord(cad2[k])-97]-v1[ord(cad2[k-1])-97])
    print(ans)
