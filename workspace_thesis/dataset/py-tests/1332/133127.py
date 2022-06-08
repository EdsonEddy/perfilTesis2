def anti_vowel(text):
    vowels=['a','e','i','o','u','y']
    res=''

    for letter in text:
        if letter not in vowels:
            res+=letter
    return res


n=input()
n2=n.lower()
n1=anti_vowel(n2)

d='.'.join(n1)
print("."+d)

