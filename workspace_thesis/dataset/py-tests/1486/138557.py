def serie ():
    global cont
    global a
    global b
    if i%2==0:
        x=cont*2
        cont=cont+1
    else:
        x=a+b
        a=b
        b=x
    return(x)
cont=1
a=1
b=0
n= int(input())
for i in range (1,n+1,1):
    s=serie()
    print(s)