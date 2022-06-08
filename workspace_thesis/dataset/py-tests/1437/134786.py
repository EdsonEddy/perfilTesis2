n = int( input() )
sw = 0
while(n>0):
   if( n%10!=7 and n%10!=4 ):
      sw = 1
   n = n // 10
if(sw):print('N')
else:  print('S')