suffocation=int(input())
death=input().split()
max=0
for j in death:
    b=death.count(j)
    if b>max:
        max=b
        defi=j
t=len(death)-max
print(t)
