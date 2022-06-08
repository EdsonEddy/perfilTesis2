n=str(input())
d=0
s=0
st=0
for j in n:
    st=st+int(j)
for i in range(len(n)-1):
    s=s+int(n[i])
    if s%3==0 and (st-s)%3==0:
        d=d+1
print(d)