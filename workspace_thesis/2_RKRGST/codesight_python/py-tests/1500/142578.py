input()
v = [int(x) for x in input().split()]
print('SI' if v == list(reversed(v)) else 'NO')