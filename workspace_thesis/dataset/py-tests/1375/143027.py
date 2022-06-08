n = input()
n = n.lower()
index = -1
for i in range(len(n)-2):
    if n[i]== 'o' and n[i+1]=='r' and n[i+2]=='o':
        index = i
        break
if index!=-1:
    print(index,index+2)
else:
    print(index)