a, b, c = map(int, input().split())
hrs=a*3600
min=b*60
s=c
nuevo=hrs+min+s+1
hrs=int(nuevo/3600)
x=nuevo%3600
min=int(x/60)
seg=x%60
if hrs<10:
    print("0", hrs, sep="", end=":")
elif hrs==24:
    print("00", end=":")
else:
    print(hrs, end=":")
if min<10:
    print("0", min, sep="", end=":")
else:
    print(min, end=":")
if seg<10:
    print("0", seg, sep="")
else:
    print(seg)    
