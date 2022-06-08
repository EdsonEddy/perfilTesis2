a=input()
if (len(a)%2!=0):
    b=len(a)//2
    a=int(a)
    a//=10**b
    a=a%10
    print(a)
else:
    print("*")

