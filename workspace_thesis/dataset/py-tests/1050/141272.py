m=0
while(m != ""):
    m=int(input())
    h=int(bin(m)[2:])
    h=str(int(h))
    cadeniv = h[::-1]
    n=int(str(cadeniv))
    print(int(str(n),2))