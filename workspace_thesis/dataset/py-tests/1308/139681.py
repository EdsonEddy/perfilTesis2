n = 25
m = 25
memo = [[-1 for x in range(n)] for y in range(m)]

def superSum(k, n):
    if k == 0:
        return n
    if memo[k][n] != -1:
        return memo[k][n]
    sum = 0
    for i in range(n):
        sum = sum + superSum(k - 1, (i + 1))
    memo[k][n] = sum
    return sum 

def main():


    while True:
        try:
            k, n = map(int, input().split())
            print(superSum(k, n))
        except EOFError:
            break

main()