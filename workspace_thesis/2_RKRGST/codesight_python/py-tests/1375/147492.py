c = input()
c = c.lower()
v = []
b = 0
for i in range(len(c)):
    if c[i] == "o":
        if c[i+1] == "r":
           if c[i+ 2] == "o":
              print(i,i+2)
              b = 1
              break
              
        else:
            print(-1)
    else:
        b = -1
if b == -1:
    print(b)
        
        
              
            
    
    