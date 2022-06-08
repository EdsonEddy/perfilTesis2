import sys
for i in sys.stdin:
    n=int(i)
    c=1
    sp=0
    si=0
    si1=0
    sp1=0
    while n>0:
        #n=n//10
        if c%2!=0:
            si=n%10
            si1=si+si1
            c=c+1
            #print(si,si1)
        else:
            sp=n%10
            sp1=sp+sp1
            c=c+1
            #print(sp,sp1)
        n=n//10
    if si1==sp1:
        print("SI")
    else:
        print("NO")
