s=0
while s!="":
    s=int(input())
    d={1:"unu",2:"du",3:"tri",4:"kvar",5:"Kvin",6:"ses",7:"Sep",8:"OK",9:"Nau",10:"dek",20:"dudek",30:"tridek",40:"kvardek",50:"Kvindek",60:"sesdek",70:"Sepdek",80:"OKdek",90:"Naudek"}
    if len(str(s))==1 or s%10==0:
        print(d[s])
    else:
        x=(s//10)*10
        y=s%10
        print(d[x],d[y])