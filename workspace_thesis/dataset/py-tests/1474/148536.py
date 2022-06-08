def Lee(v,n):
    for i in range(n):
        x=input()
        v.append(x)
n=int(input())
v1=input().split()
v2=input().split()
A=[ ]
Lee(A,n)
for i in range(n):
    if(A[i]=="+"):
        v1[i]=int(v1[i])+int(v2[i])
    else:
        if(A[i]=="*"):
            v1[i]=int(v1[i])*int(v2[i])
        else:
            if(A[i]==">"):
                if(int(v2[i])> int(v1[i])):
                    v1[i]=v2[i]
            else:
                if(A[i]=="<"):
                    if(int(v2[i])< int(v1[i])):
                        v1[i]=v2[i]
for i in range(n):
    print(v1[i])