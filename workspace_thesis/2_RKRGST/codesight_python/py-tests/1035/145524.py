frase = ""
nfrase = ""
while frase != "#":
    frase = input()
    long = len(frase)
    if frase != "#":
        for i in range (long):
            char = frase[i]
            if char == " ":
               char = "%20"
               nfrase = nfrase + char
            elif char == "!":
                char = "%21"
                nfrase = nfrase + char
            elif char == "$":
                char = "%24"
                nfrase = nfrase + char
            elif char == "%":
                char = "%25"
                nfrase = nfrase + char
            elif char == "(":
                char = "%28"
                nfrase = nfrase + char
            elif char == ")":
                char = "%29"
                nfrase = nfrase + char
            elif char == "*":
                char = "%2a"
                nfrase = nfrase + char
            else:
                nfrase = nfrase + char
        print(nfrase)
        nfrase = ""