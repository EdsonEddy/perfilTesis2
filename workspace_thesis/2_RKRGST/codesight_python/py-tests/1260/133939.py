c=int (input())
for j in range (c):
    num1,num2=map (int,input ().split ())
    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    while b!=0:
        res=b
        b=a%b
        a=res
    print (res)