while(True):
    cad = input()
    if cad=='end':
        break
    aux = cad
    n = len(cad)
    cad = cad + '***'
    flag = False
    contv = 0
    contc = 0
    for i in range(n):
        if cad[i]=='a' or cad[i]=='e' or cad[i]=='i' or cad[i]=='o' or cad[i]=='u':
            flag = True
            contv+=1
            contc = 0
        else:
            contc+=1
            contv = 0
        if contc==3 or contv==3:
            flag = False
            break
        if (cad[i]!='e' and cad[i]!='o') and cad[i]==cad[i+1]:
            flag = False
            break
    if flag == True:
        print('<{:s}> is acceptable.'.format(aux))
    else:
        print('<{:s}> is not acceptable.'.format(aux))
