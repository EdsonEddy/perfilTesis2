import sys                   
import math                  
for casos in sys.stdin:      
    n = int(casos)           
    r = math.sqrt(5)         
    f = (1+r)                
    fn = (1-r)               
    p = math.pow(f,n)        
    pn = math.pow(fn,n)      
    d = math.pow(2,n)        
    dt = (d*r)               
    n = (p - pn)             
    t = n/dt                 
    print(int(t))            