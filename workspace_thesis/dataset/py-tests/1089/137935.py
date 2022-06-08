n = int(input())
aux = n
c = 0
while n > 0 :
    r = (n // 10) *10
    dig = n - r
         
    n = n // 10
    c = c + 1
if c % 2 == 1:
    c = c + 1
    p = c / 2
    while p > 0:
        r = (aux // 10) *10
        dig = aux - r
             
        aux = aux // 10
        p = p - 1
    print (dig)
else:
    print("*")