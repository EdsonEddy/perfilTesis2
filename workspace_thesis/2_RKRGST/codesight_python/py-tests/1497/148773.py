def fun(c):
    x = ord(c)
    bin= []
    while (x > 0):
        if (x & 1) == 1:
            bin.append("1")
        else:
            bin.append("0")
        x = x >> 1
    bin.reverse()
    binary = "".join(bin)
    chu = (8 - len(binary)) * '0'
    return chu + binary
String =str(input())
#binary=[0,0,1,1,0,0]
binary = []
for c in String:
    binary.append(fun(c))
#print(binary[1][2]
print("".join(binary),end="")