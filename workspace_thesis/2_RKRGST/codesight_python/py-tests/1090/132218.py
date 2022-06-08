n = int(input())
j = 3
s = 0
while j<n:
    if j%3==0:
        s=s+j
        j=j+1
    else:
        j=j+1
print(s)