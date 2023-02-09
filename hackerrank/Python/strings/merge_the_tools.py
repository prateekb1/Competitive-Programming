def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        a = string[i:i+k]
        out = ''
        for x in a:
            if x not in out:
                out += x
        print(out)
        i += k