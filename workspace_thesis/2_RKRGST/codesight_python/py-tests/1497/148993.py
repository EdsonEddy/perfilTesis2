def invertir(a):
    b=''
    while (a // 2) != 0:
        b,a= (str(a % 2) + b),a//2
    return str(a)+b
n=input()
c=''
for i in n:
    m=ord(i)
    j=invertir(m)
    while len(j)!=8:
        j='0'+j
    c+=j
print(c)