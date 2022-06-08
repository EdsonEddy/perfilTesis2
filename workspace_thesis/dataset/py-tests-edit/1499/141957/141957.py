a, lst = int(input()), input().split()
 
lst = [int(ch) for ch in lst]
 
def f(m, n, flag):
    if flag == 1:
        return m < n
    elif flag == 2:
        return m == n
    else:
        return m > n
 
 
def is_modal(a, lst):
    flag = 1
    for i in range(1, a):
        if f(lst[i - 1], lst[i], flag):
            continue
        else:
            if flag == 3:
                return "NO"
            flag += 1
            if f(lst[i - 1], lst[i], flag):
                continue
            else:
                if flag == 3:
                    return "NO"
                flag += 1
                if f(lst[i - 1], lst[i], flag):
                    continue
                else:
                    return "NO"
    return "SI"
 
print(is_modal(a, lst))