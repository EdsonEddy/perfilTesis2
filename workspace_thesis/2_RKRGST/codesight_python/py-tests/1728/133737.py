import math
while True:
    x = int(input())
    sum = 0
    if x > 1000:
        ex = round(math.log10(x))
        for i in range(ex+1):
            digit = x//(10**(ex-i))
            x = x%(10**(ex-i))
            if digit % 2 == 0:
                sum += digit
        #     print(digit,x)
        print(sum)