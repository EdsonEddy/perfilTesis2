input()
v = [int(x) for x in input().split()]
print('SI' if v==v[::-1] else 'NO')