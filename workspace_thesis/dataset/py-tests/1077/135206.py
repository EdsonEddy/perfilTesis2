import math
h=1
while h==1:
    num=int(input())
    if num==0:
        h=0
    else:
        M=int(num/1000)
        c0=num%1000
        C=int(c0/100)
        d0=c0%100
        D=int(d0/10)
        U=d0%10
        print(num, "=>", sep=" ", end=" ")
        if M==3:
            print("mmm", end="")
        elif M==2:
            print("mm", end="")
        elif M==1:
            print("m", end="")
        if C==9:
            print("cm", end="")
        elif C==8:
            print("dccc", end="")
        elif C==7:
            print("dcc", end="")
        elif C==6:
            print("dc", end="")
        elif C==5:
            print("d", end="")
        elif C==4:
            print("cd", end="")
        elif C==3:
            print("ccc", end="")
        elif C==2:
            print("cc", end="")
        elif C==1:
            print("c", end="")
        if D==9:
            print("xc", end="")
        elif D==8:
            print("lxxx", end="")
        elif D==7:
            print("lxx", end="")
        elif D==6:
            print("lx", end="")
        elif D==5:
            print("l", end="")
        elif D==4:
            print("xl", end="")
        elif D==3:
            print("xxx", end="")
        elif D==2:
            print("xx", end="")
        elif D==1:
            print("x", end="")
        if U==9:
            print("ix")
        elif U==8:
            print("viii")
        elif U==7:
            print("vii")
        elif U==6:
            print("vi")
        elif U==5:
            print("v")
        elif U==4:
            print("iv")
        elif U==3:
            print("iii")
        elif U==2:
            print("ii")
        elif U==1:
            print("i")
        else:
            print("")