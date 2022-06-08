n=int(input())#Numero de casas que el duende Visito
PesoSaco=0
if 0 <= n <= 10**2:
    while n > 0:
        n=n-1
        p=int(input())#Numero de personas en cada casa
        if  0 <= p <= 10**2:
            while p > 0:
                p=p-1
                a,r=map(int,input().split())#0 si se porto mal 1 si se porto bien r es numero de regalos pedidos
                sw=False
                if (a==1 or a==0) and 0<=r<=10:
                        while r > 0:
                            r=r-1
                            if a==1:
                                regalo,peso=map(str,input().split())
                                peso=float(peso)
                                for i in range(0, len(regalo)):#Corroborar si regalo esta dentro del acuerdo
                                    if (regalo[i].islower() or regalo[i].isupper() or regalo[i].isnumeric()) and regalo[i]!='ñ' and regalo[i]!=' ':
                                         sw=True
                                    else:
                                         sw=False
                                         break
                                if sw==True:
                                    PesoSaco=PesoSaco+peso
                                else:
                                    break
                            else:
                                regalo, peso = map(str, input().split())
                                peso = float(peso)
                                for i in range(0, len(regalo)):  # Corroborar si regalo esta dentro del acuerdo
                                    if (regalo[i].islower() or regalo[i].isupper() or regalo[i].isnumeric()) and regalo[i] != 'ñ' and regalo[i]!=' ':
                                        sw = True
                                    else:
                                        sw = False
                                        break
                                if sw == True:
                                    continue
                                else:
                                    break
                        if a==0:
                            PesoSaco = PesoSaco+0.5
                        else:
                            continue
    print(round(PesoSaco,2))
