n=int(input())

while (n>0):
    sw=0
    x=int(input())
    
    while(x>0):
        aux=x
        m=x%100
        if(m==96):
            sw=1
            x=0
        x=x//10
         
            
    if (sw==0):
        print ("TE SALVAS :D")
    else:
        print ("APLAZADO!")   
    n=n-1
        