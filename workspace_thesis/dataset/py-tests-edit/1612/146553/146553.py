w=1
while w==1:
    p=input()
    cont="A"
    for k in range (26):
        c=0
        for j in p:
            if j==cont:
                c=c+1
        if c>0:
            print(cont,"=",c,sep="")
        a=ord(cont)
        a=a+1
        cont=chr(a)
    print("")