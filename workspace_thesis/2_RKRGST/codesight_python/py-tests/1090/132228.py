can=int(input())
i=int(3)
sum=int(0)
while(i<can):
        if(i%3==0):
                sum+=i
                i+=1
        else:
                i+=1
print(sum)