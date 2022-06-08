n=int(input())
for i in range(n):
     s=int(input())
     r=str(bin(s))
     x=r.count("11")
     print(x)
