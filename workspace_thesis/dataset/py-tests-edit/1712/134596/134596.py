s=0
n=input()
while n!="fin":

    for j in range(int(n)):
        x=int(input())
        s+=x
    print(s)
    s=0
    n = input()