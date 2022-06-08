palabra=input()
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nuevo=[]
for a in palabra:
	if a in letras:
		letras.remove(a)
if len(letras)!=0:
	mini=min(letras)
	print(mini)
else:
	print('-1')
	
	