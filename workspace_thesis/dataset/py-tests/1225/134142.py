a, b, c = map(int,input().split())

if(a>c and a>b) or (a>b and a>c):
    print(a)
elif(b>a and b>c) or (b>c and b>a):
    print(b)
else: print (c)