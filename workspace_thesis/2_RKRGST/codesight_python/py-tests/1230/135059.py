a = int(input(''))

h = int(a/3600)
m = int((a-h*3600)/60)
s = int(a-(h*3600+m*60))

print(str(h)+' '+str(m)+' '+str(s))