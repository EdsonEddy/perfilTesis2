a, b, c= map(int,input().split())
if(a<b and b<c and a<c):
    print(a,b,c)
elif(a<b and b>c and a<c):
    print(a,c,b)
elif(a>b and b<c and a<c):
    print(b,a,c)
elif(a<b and b>c and a>c):
    print(c,a,b)
elif(a>b and b<c and a>c):
    print(b,c,a)
elif(a>b and b>c and a>c): 
    print(c,b,a)
elif(a>b and b<c and a==c):
    print(b,a,c)
elif(a==b and b>c and a>c):
    print(c,a,b)
elif(a<b and b==c and a<c):
    print(a,b,c)