def marsExploration(s):
    n = len(s)
    ct = 0
    s1 = "SOS" * (n // 3)
    for i in range(len(s)):
        if s[i] != s1[i]:
            ct += 1
    return ct

s = "SOSOOSOSOSOSOSSOSOSOSOSOSOS" # 3
s = "SOSSOT" # 1
print(marsExploration(s))