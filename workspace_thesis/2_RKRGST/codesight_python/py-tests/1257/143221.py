n=int(input())
for i in range (n):
    for j in range (2):
        cad1=input()
        cad2=input()
        v=[0 for t in range(260)]
        prub=True
        for p in range(len(cad1)):
            v[ord(cad1[p])]+=1
        for q in range(len(cad2)):
            v[ord(cad2[q])]-=1
            if v[ord(cad2[q])]<0:
                prub=False
        if prub==True:
            print("Si")
        else:
            print("No")
