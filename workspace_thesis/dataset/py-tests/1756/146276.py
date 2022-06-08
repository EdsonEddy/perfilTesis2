n=int(input())
while n>0:
    secu=int(input())
    a=1
    secu=secu%6
    for k in range(secu+1):
        a=a*2
        if a>9 or a==10:
            a=(a%10)+(a//10)   
    print(a)
                
    
