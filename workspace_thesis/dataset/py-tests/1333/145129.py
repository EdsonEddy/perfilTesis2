palabra=input()
li=[]
for i in range(len(palabra)):
    new=palabra[i:]
    li.append(new)
li.sort()
for i in li:
    print(i)