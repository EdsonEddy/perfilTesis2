n=int(input()) 
while n<1000000: 
    c=0 
    m='si' 
    x=' ' 
    v=int(input()) 
    x=input().split() 
    for i in range(0,v-1):
        if m=='si': 
            if int(x[i])<int(x[i+1]):
                m='no' 
        else: 
            if int(x[i])>int(x[i+1]): 
                
                m='si' 
                c=c+1 
    print(c) 
