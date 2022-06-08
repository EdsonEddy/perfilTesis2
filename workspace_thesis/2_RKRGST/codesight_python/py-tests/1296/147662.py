casos=int(input())
l=[]
while casos > 0:
    casos-=1
    s=str(input())
    l.append(s[::-1])
l=l[::-1]
for i in l:
    print(i)