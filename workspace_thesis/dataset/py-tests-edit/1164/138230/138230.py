x = input()
s = set()
y = ''
for i in x:
   if i==' ':
      s.add(y)
      y=''
   else: y += i
c = 0
v = sorted(s)
for i in v:
   c += 1
   if(c!=len(s)):print(i,end=' ')
   else: print(i)
