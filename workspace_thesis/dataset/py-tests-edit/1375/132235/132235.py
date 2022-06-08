x = input().upper()
pos = -1
for i in range(len(x)-2):
   if(x[i]=='O' and x[i+1]=='R' and x[i+2]=='O'):
      pos = i 
      break;
if pos!=-1:print(pos,(pos+2))
else: print(pos)