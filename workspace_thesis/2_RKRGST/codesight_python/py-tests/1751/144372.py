x=input()
s=0
i=0
while i<len(x):
    if x[i]=="c" or x[i]=="C":
        s=s+1
    i=i+1
print(s)
