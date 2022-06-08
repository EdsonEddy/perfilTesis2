from sys import *
while(1):
	# numero = int ( input( 'Ingrese un numero entre 1 a 3399: ') )
	numero = int(input())
	if(numero==0):break
	# print('El numero', numero ,'en Romano es: ',end='')
	print(numero,'=> ',end='')
	while( numero >= 1000 ):
	   print('m',end='')
	   numero = numero - 1000
	if( numero >= 900 ):
	   print('cm',end='')
	   numero = numero - 900
	if( numero >= 500 ):
	   print('d',end='')
	   numero = numero - 500
	if( numero >= 400 ):
	   print('cd',end='')
	   numero = numero - 400 
	while( numero >= 100 ):
	   print('c',end='')
	   numero = numero - 100
	if( numero >= 90 ):
	   print('xc',end='')
	   numero = numero - 90  
	if( numero >= 50 ):
	   print('l',end='')
	   numero = numero - 50 
	if( numero >= 40 ):
	   print('xl',end='')
	   numero = numero - 40 
	while( numero >= 10 ):
	   print('x',end='')
	   numero = numero - 10
	if( numero >= 9 ):
	   print('ix',end='')
	   numero = numero - 9
	if( numero >= 5 ):
	   print('v',end='')
	   numero = numero - 5
	if( numero >= 4 ):
	   print('iv',end='')
	   numero = numero - 4
	while( numero >= 1 ):
	   print('i',end='')
	   numero = numero - 1  
	print()