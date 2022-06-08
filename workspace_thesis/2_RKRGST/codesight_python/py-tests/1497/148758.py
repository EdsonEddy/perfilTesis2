def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
s = input()
b = string2bits(s)
s2 = bits2string(b)
print (''.join(map(str, b)))
