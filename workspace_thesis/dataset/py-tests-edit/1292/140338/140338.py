def leevectorsum (n,s):
    su=0
    v=s.split(" ")
    for i in range (n):
        su=su+ int(v[i])
    return su
n=int(input())
while n!=0:
    s=input()
    print(leevectorsum (n,s))
    n=int(input())
