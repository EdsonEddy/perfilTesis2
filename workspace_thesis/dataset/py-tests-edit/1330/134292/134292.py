s,n=map(str,input().split())
x=len(s)
o=int(x)-int(n)
palabra1=s[:o]
palabra2=s[o:]
print(palabra2+palabra1)