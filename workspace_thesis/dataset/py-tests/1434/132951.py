n = int(input())
copian = n
num = 0
while n > 0:
    num=num*10 + n%10
    n//=10
if num==copian:
    print("S")
else:
    print("N")