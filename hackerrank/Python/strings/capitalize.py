def solve(s):
    for i in s.split():
        s= s.replace(i,i.capitalize())
    return (s) 

def solve(s):
    res = []
    for i in range(len(s)):
        temp = s[i]
        if i ==0:
            temp = s[i].upper()
        if (s[i-1].isspace()) and (s[i].isalpha()):
            temp = s[i].upper()
        res.append(temp)

    return(''.join(res))


