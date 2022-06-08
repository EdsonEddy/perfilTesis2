def fact(n):
    f=1
    sw=0
    for i in range(1,n+1):
        if sw==0:
            f=f*i*(-1)
            print(f)
            sw=1
        else:
            f=f*i*(-1)
            print(f)
      


while True:
    a=int(input())
    fact(a)
