n = int(input())
s = 0
while(n>0):
    if(n%10!=4 and n%10!=7):
        s = 1
    n = n // 10
if(s==0):
    print('S')
else:
    print('N')