m=int(input())
list=input().split()
while m!=0:
    s=0
    for i in list:
        s=s+int(i)
    print(s)
    m=int(input())
    list=input().split()