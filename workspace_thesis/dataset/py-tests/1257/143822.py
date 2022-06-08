n=int(input())
for i in range(n):
    p=input()
    q=input()
    v=[0 for a in range (260)]
    flag=True
    for j in range(len(p)):
        v[ord(p[j])]+=1
    for j in range(len(q)):
        v[ord(q[j])]-=1
        if(v[ord(q[j])]<0):
            flag=False
    if(flag==True):
        print("Si")
    else:
        print("No")
      
