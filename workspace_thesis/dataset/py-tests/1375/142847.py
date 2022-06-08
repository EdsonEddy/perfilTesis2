cad = input()
cad = cad.lower()
x = -1
for i in range(0, len(cad) - 3 + 1):
    if(cad[i] == 'o' and cad[i+1] == 'r' and cad[i+2] == 'o'):
        x = i
        break
if(x != -1):
    print(x,x+2)
else:
    print(-1)
    
