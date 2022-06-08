import sys
for n in sys.stdin:
    for q in range(int(n)):
        l=[]
        i = int(input())
        l = list(map(int,input().split()))
        e=[]
        for x in l:
            if (int(x)*2)%3==0:
                e.append(x)
        s=int(0)
        for z in e:
            a=int(z)*2
            s=s+a
        print('La suma es',s)



