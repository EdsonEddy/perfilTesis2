while True:
    input_string=input()
    list = input_string.split()
    sum=0
    for num in list:
        sum+=int(num)
    print(sum)