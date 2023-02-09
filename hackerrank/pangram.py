import string
def pangrams(s):
    # Write your code here
    alpha = list(string.ascii_lowercase)
    for i in s.lower():
        if i in alpha:
            alpha.remove(i)
    if alpha:
        return "pangram"
    else:
        return "not pangram"

print(pangrams("We promptly judged antique ivory buckles for the next prize"))