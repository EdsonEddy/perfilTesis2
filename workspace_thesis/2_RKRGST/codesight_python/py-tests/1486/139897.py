f=[]

def fibo(x):
    x=int(x)
    global f # para modificar variables fuera del procedimineto
    f.append(1)#
    f.append(1)#
    c=0
    for i in range(2,x+1):
        c=f[i-1]+f[i-2]
        f.append(c)

n=int(input())
cd=0
kd=1
fibo(n)
for i in range(n):
    if(i%2==0):
        print(f[cd])
        cd+=1
    else:
        print(kd*2)
        kd+=1
        
