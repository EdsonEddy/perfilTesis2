l, r, k = map(int, input().split(" "))
cd = 0
for i in range(l,r+1,1):
    if(i % k == 0):
        cd+=1
print(cd)
