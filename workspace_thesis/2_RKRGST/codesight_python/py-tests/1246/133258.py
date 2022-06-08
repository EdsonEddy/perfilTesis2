c=input()
n=input()
k=0
for i in range(len(n)):
    r=n[i]
    if r==c:
        k=k+1
print(k)