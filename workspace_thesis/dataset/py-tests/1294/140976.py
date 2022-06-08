def main():
    n = int(input())
    j = 1
    while j <= n:    
        m,a,b = input().split()
        m,a,b = int(m),int(a),int(b)
        v = [int(x) for x in input().split()]
        sum = 0
        for i in v[a:b+1]:
            sum += i
        print(sum)
        j += 1

if __name__ == '__main__':
    main()