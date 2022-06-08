n=int(input(""))
for i in range(n):
    a=str(input(""))
    b=str(input(""))
    a=a.replace(" ","")
    b=b.replace(" ","")
    a=sorted(a)
    b=sorted(b)
    if(a==b):
        print("Si")
    else:
        print("No")