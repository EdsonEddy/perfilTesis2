n = input()
s = ''
p = n.split('0')
for i in range(len(p)):
    a = len(p[i])
    s = s + str(a)
print(s)