can=int(input())
i=int(1)
res=""
while(i<=can):
        a=input()
        lit=a.split()
        a=int(lit[0])
        b=int(lit[1])
        i+=1
        if(a>b):
                res+=">"+"\n"
        if(a<b):
                res+="<"+"\n"
        if(a == b):
                res+="="+"\n"
print(res)