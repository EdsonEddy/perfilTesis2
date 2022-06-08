from sys import stdin
for i in stdin:
    a,b=map(int,i.split())
    if a==0 and b==0:
         break;
    y=(4*a-b)/2

    y=int(y)
    x=a-y
    if x<0 or y<0 or (4*a-b)%2!=0 or y<0 :
        print('-1')
    elif (4*a-b)%2==0 or 4*a-b==0 :
        print(y,x)