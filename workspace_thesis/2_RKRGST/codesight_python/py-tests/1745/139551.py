n = float(input())
neg = 0
may = 0
cont = 0
while n!=0:
    cont = cont+1
    if n < 0:
        neg = 1 + neg
    if n > may:
        may = n
    n = float(input())

print(int((neg*100)/cont))
print(int(may))
    
