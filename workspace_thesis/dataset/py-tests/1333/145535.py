a = input()
m = ''
lista = []
n = len(a)
for x in a:
      m = m + a[n - 1]
      lista.insert(0, m)
      n = n - 1
li = []
for y in lista:
      p = y[:: - 1]
      li.append(p)
li.sort()
for z in li:
      print(z)