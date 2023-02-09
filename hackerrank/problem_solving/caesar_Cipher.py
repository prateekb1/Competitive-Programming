def caesarCipher(s, k):
    # Write your code here
    news = ''
    for i in s:
        if i.islower():
            if ord(i) + k > 122:
                diff = ord(i) + k - 122
                while diff > 26:
                    diff -= 26
                news += chr(96+diff)
            else:
                news += chr(ord(i)+k)
        elif i.isupper():
            if ord(i) + k > 90:
                diff = ord(i) + k - 90
                while diff > 26:
                    diff -= 26
                news += chr(64+diff)
            else:
                news += chr(ord(i)+k)
        else:
            news += i   
    return news


s = "159357lcfd"
k = 98
# fff.jkl.gh
print(caesarCipher(s,k))