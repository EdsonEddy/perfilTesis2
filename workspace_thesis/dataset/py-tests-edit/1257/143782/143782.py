n=int(input())
for i in range(n):
    cad=input()
    cad1=input()
    v=[0 for x in range (260)]
    # aux="ICPCUMSA"
    flag=True
    for j in range(len(cad)):
        v[ord(cad[j])]+=1
    for j in range (len(cad1)):
        v[ord(cad1[j])]-=1
        if (v[ord(cad1[j])] <0):
            flag=False
    if (flag == True):
        print ("Si")
    else:
        print ("No")
