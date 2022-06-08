for i in range(int(input())):
    n=list(input())
    for j in range(len(n)-1,-1,-1):
        print(n[j],end="")
    print(end="\n")