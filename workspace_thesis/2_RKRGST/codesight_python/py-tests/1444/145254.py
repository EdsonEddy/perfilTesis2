xs=int(input())
for sd in range(xs):
    x=int(input())
    s='0'
    sw=False
    g=0
    k=0
    for i in range(2**(len(str(x))+1),-1,-1):
        if x&(1<<i)>0:
            s=s+'1'
            sw=True
        elif sw==True:
            s=s+'0'
    while g>=0:
        if g==0:
            g=s.find('11',g)
        else:
            g=s.find('11',g+2)
 
        if g>=0:
            k=k+1
 
    print(k)