cas=int(input())
while cas>0:
    x=int(input())
    n=input().split()
    c=0
    for i in range(len(n)-2):
        if int(n[i])<int(n[i+1]) and int(n[i+1])>int(n[i+2]):
            c+=1
    print(c)
    cas-=1