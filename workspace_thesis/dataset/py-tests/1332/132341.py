n=str(input())
s=''
n=n.lower()
bf={'a','e','i','o','u','y'}
for i in n:
    if i in bf:
        i=i
    else:
        s=s+'.'+i
print(s)