n = input()
sw = True
for i in range(0,len(n)-1):
    if n[i] != n[(len(n)-1)-i]:
        sw = False
if sw:
    print("S")
else:
    print("N")