n = input()
c = 0
l =[]
m = len(n)
for i in n:
    if i == '1':
        c = c + 1
        #print(c)
    else:
        l.append(c)
        c = 0
l.append(c)
for i in l:
 print(i,end="")