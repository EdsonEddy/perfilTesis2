a,b,c=map(int,input().split())
con=0
for i in range (a,b+1,1):
    if (i%c==0):
        con+=1
print(con)




