a=int(input(""))
b=a%3600
hrs=int(a/3600)
min=int(b/60)
seg=b%60 
print (hrs, min, seg, sep=" ")