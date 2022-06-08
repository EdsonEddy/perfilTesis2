j=0
while(j!=""):
    j=int(input())
    d=int(bin(j)[2:])
    d=str(int(d))
    cadenainvertida = d[::-1]
    a=int(str(cadenainvertida))
    print(int(str(a),2))
