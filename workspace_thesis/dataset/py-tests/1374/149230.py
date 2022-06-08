a1, b1, a2, b2 = [int(x) for x in input().split()]
x = max(a1, a2)
y = min(b1, b2)
print('[]' if x > y else '[' + str(x) + ',' + str(y) +']')