x=int(input())
for i in range(x):
    y=int(input())
    c = 0
    for j in range(y):
        pal=str(input())
        pal=pal.lower()
        if pal!="porque":
            c=c+1
        else:
            print(c)