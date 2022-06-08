# Este programa convierte un numero en romano
# Orlando Wilder Apaza Flores
# 9927607
# 1.0 11/03/2019
def unidad(uni):
   if uni==1:
      return "i"
   elif uni==2:
      return "ii"
   elif uni==3:
      return "iii"
   elif uni==4:
      return "iv"
   elif uni==5:
      return "v"
   elif uni==6:
      return "vi"
   elif uni==7:
      return "vii"
   elif uni==8:
      return "viii"
   elif uni==9:
      return "ix"
   else:
      return ""

def decena(dece):
   if dece==1:
      return "x"
   elif dece==2:
      return "xx"
   elif dece==3:
      return "xxx"
   elif dece==4:
      return "xl"
   elif dece==5:
      return "l"
   elif dece==6:
      return "lx"
   elif dece==7:
      return "lxx"
   elif dece==8:
      return "lxxx"
   elif dece==9:
      return "xc"
   else:
      return ""

def centena(cen):
   if cen==1:
      return "c"
   elif cen==2:
      return "cc"
   elif cen==3:
      return "ccc"
   elif cen==4:
      return "cd"
   elif cen==5:
      return "d"
   elif cen==6:
      return "dc"
   elif cen==7:
      return "dcc"
   elif cen==8:
      return "dccc"
   elif cen==9:
      return "cm"
   else:
      return ""
   
def millar(mill):
   if mill==1:
      return "m"
   elif mill==2:
      return "mm"
   elif mill==3:
      return "mmm"
   else:
      return ""
a=int(input())
aux=a
while(a!=0):
   if a<4000 and a>0:	
      uni = a%10
      primera = unidad(uni)
      a = a//10
      dece = a%10
      segunda = decena(dece)
      a = a//10
      cen = a%10
      tercera = centena(cen)
      mill = a//10
      cuarta = millar(mill)
      print(aux ,"=>", end=" ")
      print(cuarta, end="")
      print(tercera, end="")
      print(segunda, end="")
      print(primera)
   else:
      print("ERROR")
   a=int(input())
   aux=a