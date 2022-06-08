o,r,p,s=map(float,input().split())
 
from math import sqrt
 
x=sqrt((o-p)**2+(r-s)**2)
 
print ("{0:.2f}".format (x))