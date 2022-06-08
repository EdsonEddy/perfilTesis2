n=input()
st,s,c=0,0,0
for i in n:
    st+=int(i)
for j in range(len(n)-1):
    s+=int(n[j])
    if s%3==0 and (st-s)%3==0:
        c+=1
print(c)
