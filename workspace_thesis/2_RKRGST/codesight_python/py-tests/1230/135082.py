n = int( input() )
H=3600
M=60
h=int(n/H)
n=n%H
m=int(n/M)
s=int(n%M)
print(h, m, s)