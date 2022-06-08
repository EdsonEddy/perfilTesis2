while True:
    try:
        i=int(input())
        n={1:"unu",2:"du",3:"tri",4:"kvar",5:"Kvin",6:"ses",7:"Sep",8:"OK",9:"Nau",10:"dek",20:"dudek",30:"tridek",40:"kvardek",50:"Kvindek",60:"sesdek",70:"Sepdek",80:"OKdek",90:"Naudek"}
        if i in n:
            print(n[i])
        else:
            h=str(i)
            p=int(h[0])*10
            s=int(h[1])
            print(n[p],n[s])
    except ValueError:
        break