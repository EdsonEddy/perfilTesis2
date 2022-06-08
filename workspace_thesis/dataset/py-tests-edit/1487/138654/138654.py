def primo (n):
    if n<=1:
        return False
    else:
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i=i+1
        return True
for k in range (10000):
    n=int(input())
    if primo(n)==True:
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")
            
        
        
    
    
        
        
