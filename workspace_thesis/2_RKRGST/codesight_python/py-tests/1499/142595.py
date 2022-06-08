n = int(input())
v = list(map(int, input().split()))
a = 0
b = -1
for i in range(n):
    if (v[i] > b):
        a = i
        b = v[i] 
    else:
        break
    
for i in range(a+1, n):
    if (v[i] == b):
        a = i
        b = v[i] 
    else:
        break
    
for i in range(a+1, n):
    if (v[i] < b):
        a = i
        b = v[i] 
    else:
        break
if a == n-1:
    print("SI")
else:
    print("NO")

        

    