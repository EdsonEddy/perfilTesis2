cad = input()
sw=0
for i in range(len(cad)):
    if i!= len(cad):
        if cad[i]== "o" or cad[i]== "O":
            if (i+1)!= len(cad):
                if cad[i+1]== "r" or cad[i+1]== "R":
                    if (i+2)!= len(cad):
                        if cad[i+2]== "o" or cad[i+2]== "O":
                            print(i,(i+2))
                            sw=1
                            break
if sw==0:
    print(-1)

        
