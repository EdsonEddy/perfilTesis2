password=''
while password != 'end':
    password=str(input())
    if password == 'end':
        break
    else:
        SWTieneVocal = False
        SWTieneConsecutivos = True
        SwDoble = True
        cV = 0
        cC = 0
        if 1<=len(password)<=20:
            for i in range(0,len(password)):
                if password[i] in 'aeiou':
                    SWTieneVocal=True
                    cV+=1
                    cC=0
                if password[i] in 'bcdfghjklmnpqrst':
                    cC+=1
                    cV=0
                if cV == 3 or cC == 3:
                    SWTieneConsecutivos=False
                if i<len(password)-1:
                    if password[i]==password[i+1]:
                          SwDoble=False
                    if str(password[i])+str(password[i+1])=='oo' or  str(password[i])+str(password[i+1])=='ee':
                          SwDoble = True
            if (SWTieneVocal and SWTieneConsecutivos and SwDoble)==True:
                print('<'+str(password)+'>','is acceptable.')
            else:
                print('<'+str(password)+'>','is not acceptable.')