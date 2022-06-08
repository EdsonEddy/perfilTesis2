c=str(input())
s=str(input())
if 1<=len(c)<=100:
    for i in range(0,len(c)):
        if c[i]==s:
            print(i)