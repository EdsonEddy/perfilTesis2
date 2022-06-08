f = lambda x, y : x + (' = ' if x == y else ' < ' if x < y else ' > ') + y
print(f(*input().split()))