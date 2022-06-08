import sys
for i in sys.stdin:
    x=int(i)
    if x>=0 and x<=1000:
        p=(x*2)+1
        print(p)
    else:
        break