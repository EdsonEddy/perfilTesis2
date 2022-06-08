def insercion(vec):
    for i in range(1,len(vec)):
        for j in range(i-1,-1,-1):
            if vec[j+1]>vec[j]:
                vec[j + 1], vec[j]=vec[j],vec[j+1]
            else: break
n=int(input())
while n!=0:
    v = input().split()
    insercion(v)
    cad = "".join(v)
    print(cad)
    n = int(input())