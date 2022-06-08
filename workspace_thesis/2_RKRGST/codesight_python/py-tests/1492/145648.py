t=input()
s=input()
for i in range(len(t)-1):
    k=t[:len(s)]
    if k==s:
        print(i)
    t=t[1:]