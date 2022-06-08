x=0
while(x !=" " ):
   x=int(input())
   y=int(bin(x)[2:])
   y=str(int(y))
   cadena = y[::-1]
   a=int(str(cadena))
   print(int(str(a),2))
