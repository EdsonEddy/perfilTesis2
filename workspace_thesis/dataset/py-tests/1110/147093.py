cad = input()
cad= cad.upper()
sw=True
for i in range(len(cad)):
    if (cad[i] != "A" and cad[i] != "R"):
        sw=False
        break
if sw:
    print("Chewbacca")
else:
    print("Han Solo")

        
        
