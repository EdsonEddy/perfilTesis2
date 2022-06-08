n=int(input())
pico=0
resto=0
vuelta=0
for i in range(n):
    if 0<=n<=20:
        if vuelta>0:
            print(pico,resto)
            pico=0
            resto=0
        c,p=map(int,input().split())
        vuelta=vuelta+1
        if 0<=c<=10**6 and 0<=p<=10**6:
            while True:
                if c>2 and p>1:
                    c=c-3
                    p=p-2
                    pico=pico+1
                else:
                    if p>c or c>=0 or p>=0:
                        resto=c+p
                        break
print(pico,resto)