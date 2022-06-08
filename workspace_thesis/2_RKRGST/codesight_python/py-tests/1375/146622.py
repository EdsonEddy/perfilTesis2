cad=input()
cad=cad.lower()#para convertir a minusculas
flag=False
index=-1
for i in range(len(cad)-2):#porque se busca de tres en tres y solo quiero que vayas hasta aqui 
    if(cad[i]=='o' and cad[i+1]=='r' and cad[i+2]=='o'):#
        index=i
        break
    
if(index!=-1):
    print(index,index+2)
else:
    print(-1)
    
