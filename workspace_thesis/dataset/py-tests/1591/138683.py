def primo(n):
    if n==2 or n==3 or n==5 or n==7:
        return True
    else:
        return False
t=int(input())
for i in range (t):
    x=int(input())
    num,p=0,1
    sw=False
    while x>0:
        dig=x%10
        if primo(dig)==True:
            sw=True
            num=p*(dig)+num
            p=p*10
        x=x//10    
    if sw==True:
        print(num)
    else:    
        print(-1)
