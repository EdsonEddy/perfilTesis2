cad=input()
vol="a","e","i","o","u","y","A","E","I","O","U","Y"
cd=""
for i in cad:
     if (i in vol)==False:
         cd=cd+"."+i.lower()
print(cd)