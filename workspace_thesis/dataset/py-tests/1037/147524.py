n=int(input())
for i in range(n):
    cad1=input()
    cad2=input()
    v1=[0 for k in range(26)]
    c=0
    for j in range(len(cad1)):
        v1[ord(cad1[j])-97]=j
    ans=0
    for j in range(1,len(cad2)):
        ans+=abs(v1[ord(cad2[j])-97]-v1[ord(cad2[j -1])-97])
    print(ans)
