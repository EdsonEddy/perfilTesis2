import math
a, b, c = map(int,input().split())
aa=a
bb=b
cc=c
if(aa==0):aa+=1
if(bb==0):bb+=1
if(cc==0):cc+=1
la = int( math.log10(aa) + 1)
lb = int( math.log10(bb) + 1)
lc = int( math.log10(cc) + 1)
p1 = (a*(10**lb) + b ) * (10**lc) + c
p2 = (a*(10**lc) + c ) * (10**lb) + b
p3 = (b*(10**la) + a ) * (10**lc) + c
p4 = (b*(10**lc) + c ) * (10**la) + a
p5 = (c*(10**la) + a ) * (10**lb) + b
p6 = (c*(10**lb) + b ) * (10**la) + a
#print(p1,p2,p3,p4,p5,p6)
print(max(p1,p2,p3,p4,p5,p6))
