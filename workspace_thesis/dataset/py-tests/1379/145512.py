#min = ['123','124', '56','90']
n = int(input())

#print(m)
while n !=0:
    min = input().split()
    mi = sorted(min)
    ge = mi[::-1]
    m = "".join(ge)
    print(m)
    n=int(input())
    if n==0:
        break