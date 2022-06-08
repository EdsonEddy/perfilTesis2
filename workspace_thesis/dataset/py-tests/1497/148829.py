def ascii_to_bin(char):
    ascii = ord(char)
    bin = []
    while (ascii > 0):
        if (ascii & 1) == 1:
            bin.append("1")
        else:
            bin.append("0")
        ascii = ascii >> 1
    bin.reverse()
    bin = "".join(bin)
    zerofix = (8 - len(bin)) * '0'
    return zerofix + bin
String =str(input())
bin = []
for char in String:
    bin.append(ascii_to_bin(char))

print("".join(bin),end="")
