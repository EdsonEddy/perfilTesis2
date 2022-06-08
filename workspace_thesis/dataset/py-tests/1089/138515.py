a=input()
if (len(a)%2!=0):
    b=len(a)//2
    a=int(a)
    a//=1|0**b
    a=a%10
    print(a)
else:
    print("*")
