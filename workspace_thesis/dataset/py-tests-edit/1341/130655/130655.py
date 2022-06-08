x=input()
while x !="" \
          "":
    a=-1
    b=1
    for i in range(int(x)+1):
        c=a+b
        a=b
        b=c
    print(c)
    x=input()
