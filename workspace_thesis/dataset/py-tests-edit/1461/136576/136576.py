def get_squared_digit_sum(num):
    res=0
    for digit in num:
        res= res + pow(int(digit),2)
    return res
def is_happy(n):
    if n == 4:
        return False
    u= get_squared_digit_sum(list(str(n)))
    if u==1:
        return True
    else:
        return is_happy(u)
casos=int(input())
for i in range(casos):
    g=int(input())
    if is_happy(g)==True:
        print("Feliz")
    else:
        print("Triste")