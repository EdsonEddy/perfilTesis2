from sys import stdin
num = ['unu', 'du', 'tri', 'kvar', 'Kvin', 'ses', 'Sep', 'OK', 'Nau', 'dek']
for line in stdin:
    s = ''
    if int(line) % 10 == 0 and int(line) > 10:
        s = s + num[int(line[0])-1] + 'dek'
    elif 10 < int(line) < 20:
        s = s + 'dek ' + num[int(line[1])-1]
    elif 10 < int(line):
        s = s + num[int(line[0]) - 1] + 'dek ' + num[int(line[1]) - 1]
    else:
        s = s + num[int(line)-1]
    print(s)