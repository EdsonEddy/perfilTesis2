c,r=map(str,input().split())
for i in range (int(r)):
    c=c[len(c)-1]+c[:(len(c)-1)]
print(c)