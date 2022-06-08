cad=input()
sw=False
p1=0
p2=0
for i in range(len(cad)-2):
  if cad[i]=='O' or cad[i]=='o':
    if cad[i+1]=='R' or cad[i+1]=='r':
      if cad[i+2]=='O' or cad[i+2]=='o':
        sw=True
        p1=i
        p2=i+2
        break
if sw:
  print(str(p1)+" "+str(p2))
else:
  print("-1")