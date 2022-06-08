import math
while True:
    n=int(input())
    a=0
    for i in range(1,n+1,+1):
        a=a+math.log10(i)
    facto=int(a+1)
    print(facto)
