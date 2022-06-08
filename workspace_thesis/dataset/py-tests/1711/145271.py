n=int(input())
while n>0:
    sumaT = 0
    def suma_digitos(num):
        s = 0
        while num > 0:
            s = s + num
            break
        return s
    m = int(input())
    while m >0:
        num=int(input())
        sumaT=sumaT+suma_digitos(num)
        m=m-1
    print(sumaT)
    n=n-1