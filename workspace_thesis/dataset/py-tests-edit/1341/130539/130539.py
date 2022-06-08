n=input()
while n !="" \
          "":
    a=-1
    b=1
    for i in range(int(n)+1):
        c=a+b
        a=b
        b=c
    print(c)
    n=input()