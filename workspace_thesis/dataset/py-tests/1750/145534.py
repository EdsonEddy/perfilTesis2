from sys import stdin,stdout
for cad in stdin:
    cad = list(map(str,cad.split()))
    cad = cad[0]
    c = ''
    flag = False
    for i in range(int(len(cad)/2)):
        c = c+cad[i]
        mx = cad.rfind(c)
        if mx+i+1==len(cad):
            flag = True
            break
    if flag==True:
        stdout.write('si\n')
    else:
        stdout.write('no\n')