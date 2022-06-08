import math
n=1
while n!=0:
    n=int(input())
    s=n
    r=""
    while s!=0:
        while s>=1000:
            s=s-1000
            r=r+"m"
        while s>=400:
            if s//900==1:
                s=s-900
                r=r+"cm"
            if s//500==1:
                s=s-500
                r=r+"d"
            if s//400==1:
                s=s-400
                r=r+"cd"
        while s>=100:
            s=s-100
            r=r+"c"
        while s>=40:
            if s//90==1:
                s=s-90
                r=r+"xc"
            if s//50==1:
                s=s-50
                r=r+"l"
            if s//40==1:
                s=s-40
                r=r+"xl"
        while s>=10:
            s=s-10
            r=r+"x"
        while s>=4:
            if s//9==1:
                s=s-9
                r=r+"ix"
            if s//5==1:
                s=s-5
                r=r+"v"
            if s//4==1:
                s=s-4
                r=r+"iv"
        while s>=1:
            s=s-1
            r=r+"i"
        print(n,"=>",r)