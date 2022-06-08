n=str(input())
s=""
for i in n:
    s=s+i
    if len(s)==8:
        s=int(s,2)

        f=chr(s)
        print(f,end="")
        s=""
print()