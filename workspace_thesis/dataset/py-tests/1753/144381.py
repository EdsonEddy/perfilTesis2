def capicuo(cad):
    cad2=""
    n=len(cad)
    for i in range (n):
        cad2=cad[i]+cad2
    if cad2==cad:
        return 1
    else:
        return 0

x= input()
s=0
v= x.split()
for ele in v:
    s=s+capicuo(ele.lower())
print (s)
