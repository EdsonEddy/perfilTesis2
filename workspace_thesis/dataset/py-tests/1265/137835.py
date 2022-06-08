n=int(input())
l=int(n/240)
ll=n%240
c=int(ll/12)
p=ll%12
print("(", end="")
print(l, c, p, sep=", ", end="")
print(")")