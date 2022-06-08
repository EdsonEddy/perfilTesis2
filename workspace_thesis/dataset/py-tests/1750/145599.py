i = 0

while i == 0:
    cad = input()
    n = len(cad)
    a = cad[0]
    b = cad[1]
    if ((cad[n-1] == b) and (cad[n-2] == a)):
        print("si")
            
    else:
        print("no")
    