x = int(input())
print('hace frio' if x < 10 else 'hace calor' if x > 30 else 'esta bien')
if x < 1:
	print('se congela')
elif x > 99:
	print('hierve')