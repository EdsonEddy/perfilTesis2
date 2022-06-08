import sys
def ans(num,den):
   if num > 100000:return 0
   v = [1] * 10   
   while num:
      c = num % 10
      if v[c]==0:return 0
      v[c] = 0
      num = num // 10
   while den:
      c = den % 10
      if v[c]==0:return 0
      v[c] = 0
      den = den // 10
   return 1
for x in sys.stdin:
   N = int(x)
   sw = 1
   for den in range(1234,50000):
      num = den * N
      if num > 98765:break
      numerador = num
      denominador = den
      if num < 10000:numerador = num * 10
      if den < 10000:denominador = den * 10
      if ans(numerador,denominador):
         print(num,'/',den,N)
         sw = 0         
   if sw:print('No hay soluciones para',N)