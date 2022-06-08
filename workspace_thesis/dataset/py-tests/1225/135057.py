a, b, c = map(int, input().split())
if(a>b):
    m1=a
    m2=b
else:
    m1=b
    m2=a
if(c>m2):
    m3=m2
    m2=c
else:
    m3=c
if(c>m1):
    x=m1
    m1=c
    m2=x
print(m1)