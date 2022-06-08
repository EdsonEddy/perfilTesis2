

m=int (input())
for i in range (1,m+1,1):
    a, b = map(int, input().split(" "))
    if (a>=2 and b>=2 and b<10**5 and a<=10**5):

        while a != b:
            if a > b:
                a=a-b
            else:
                b=b-a    
    print (a)

