n=[]
for i in range(int(input())):
    n.append(list(input()))
for j in range(len(n)-1,-1,-1):
    for k in range(len(n[j])-1,-1,-1):
        print(n[j][k],end="")
    print(end="\n")  