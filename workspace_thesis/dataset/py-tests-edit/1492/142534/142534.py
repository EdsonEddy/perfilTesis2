t=str(input())
c=input()
tam=len(t)
if(tam>=0 and tam<=100):
    for i in range(tam):
        if(t[i]==c):
            x=i
            print(x)