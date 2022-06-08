import re, string

def sinsigno ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

s=str(input())
print(sinsigno(s))
