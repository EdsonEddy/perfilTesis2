m,v=map(int,input().split())
while 0<=m<=20:
    if 0<=v<=50:
        k=input().split()
        e=int(k[m-1])
        z=len(k)
        s=0
        z=z-1
        for i in range(0,z,1):
            y=int(str(k[i]))
            M=y*v**z
            s=s+M
            z=z-1
        else:
            print(float(s+e))
            m, v = map(int,input().split())