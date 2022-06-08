x=int(input())
fact,sw=1,True
for i in range(1,x+1):
    fact*=i
    if sw:
        print(-fact)
        sw=False
    else:
        print(fact)
        sw=True