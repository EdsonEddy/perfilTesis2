import sys
for bit in sys.stdin:
    bit = int(bit)
    bit = bin(bit)
    bit = bit.lstrip("0b")
    bit = str(bit)
    bit = len(bit)
    print(bit)
