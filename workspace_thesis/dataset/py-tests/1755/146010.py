casos=int(input())
while casos > 0:
        casos-=1
        a,b=map(int,input().split())
        s=0
        l=[]
        for i in range(0,b):
            l.append(1)
        j=0
        while True:
               for u in range(0,b):
                 s=s+l[j+u]
               l.append(s)
               j=j+1
               s=0
               if j == 40:
                   break
        print(l[a])