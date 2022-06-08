x=input()
t=int(x) 
x=int
a= (t)//3600 
s= (t - (a*3600))//60 
c= t - (a*3600) - (s*60)
print( a, s,c)