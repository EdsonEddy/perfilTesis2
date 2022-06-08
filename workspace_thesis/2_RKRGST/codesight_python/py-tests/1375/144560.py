x = input()
x = x.lower()
sw = True
for i in range(len(x)):
    if i <= len(x)-3:
        if x[i]=='o' and x[i+1]=='r' and x[i+2]=='o':
            print(i,i + 2)
            sw = False
if sw:
    print(-1)

