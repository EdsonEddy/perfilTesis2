a, b = map(int, input().split())
c = 0
if (a == b):
    print(1)
if (a != b):
    for x in range(a+1, b):
        for i in range(2, x):
            if x%i != 0:
            
                continue
            else:
                
                break 
        else:
           
            c = c + 1
        
        
    print(c)

