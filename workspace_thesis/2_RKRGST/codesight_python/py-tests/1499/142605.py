n = int(input())
v = list(map(int, input().split()))
prev = -1
index = 0
for i in range(n):
    if(v[i] > prev):
        index = i
        prev = v[i]
    else:
        break
for i in range(index+1, n):
    if(v[i] == prev):
        index = i
        prev = v[i]
    else:
        break
for i in range(index+1, n):
    if(v[i] < prev):
        prev = v[i]
        index = i
    else:
        break
 
if(index == n-1):
    print("SI")
else:
    print("NO")