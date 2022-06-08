n=int(input())
for i in range(n):
    cad=input()
    cad=cad.replace(" ","")
    tam=len(cad.lower())
    s=0
    s1=0
    for j in range(tam):
        p=ord(cad[j])
        s=s+p
    cad=input()
    cad=cad.replace(" ","")
    tam=len(cad.lower())
    for j in range(tam):
        p=ord(cad[j])
        s1=s1+p
    if s==s1:
        print("Si")
    else:
        print("No")
