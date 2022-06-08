n=int(input())

for i in range(n):
    cad1=input()
    cad2=input()
    v=[0 for x in range(260)]
    sw=True
    for j in range(len(cad1)):
        v[ord(cad1[j])]+=1
    
    for j in range(len(cad2)):
        v[ord(cad2[j])]-=1
        if(v[ord(cad2[j])]<0):
            sw=False
    if(sw==True):
        print("Si")
    else:
        print("No")