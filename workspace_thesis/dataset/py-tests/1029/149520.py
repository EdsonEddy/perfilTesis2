def todo(v):
    aux1=[]
    aux2=[]
    for i in range (len (v)):
        if i%2==0:
            x=v[i]
            aux1.append(x)
        else:
            x=v[i]
            aux2.append(x)
    s1,s2=0,0
    for j in range (len (aux1)):
        s1=s1+aux1[j]
    for j in range (len (aux2)):
        s2=s2+aux2[j]

    return(s1-s2)
while True:
    v=list(map(int,input().split()))
    v.sort(reverse=True)
    print(todo(v))