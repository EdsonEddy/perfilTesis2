n = int (input())
c = n
nnum = 0
while n > 0:
    nnum = nnum * 10 + n % 10
    n //= 10
if nnum == c:
    print("S")
else :
    print("N")
