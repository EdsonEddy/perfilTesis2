import sys
for q in sys.stdin:
    for w in range(int(q)):
        n=input()
        l=[]
        count=int(0)
        for e in n:
            for i in range(1,int(e)+1):
                if int(e)%int(i)==0:
                    count+=1
            if count==2:
                l.append(e)
                count=0
            else:
                count=0
        algo = "".join(l)
        if len(l)==0:
            print(-1)
        else:
            print(algo)

