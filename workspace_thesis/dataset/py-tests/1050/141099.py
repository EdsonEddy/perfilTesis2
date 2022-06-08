y=0
while(y !=" "):
    y=int(input())
    c=int(bin(y)[2:])
    c=str(int(c))
    cadenainvertida = c[::-1]
    b=int(str(cadenainvertida))
    print(int(str(b),2))