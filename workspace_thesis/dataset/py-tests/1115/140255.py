n=input()
c=0
s=0
sd=0
for i in n:
    s=s+int(i)
for i in n[:len(n)-1]:
    sd=sd+int(i)
    if sd%3==0 and (s-sd)%3==0:
        c+=1
print(c)

