def anti_vowel(text):
    vowels=['a','e','i','o','u','y']
    pos=''
    for letter in text:
        if letter not in vowels:
            pos+=letter
    return pos
a=input()
n2=a.lower()
n1=anti_vowel(n2)
d='.'.join(n1)
print("."+d)