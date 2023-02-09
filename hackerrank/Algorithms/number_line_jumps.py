def kangaroo(x1, v1, x2, v2):
    # Write your code here
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

    # METHOD 2
    # return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'

print(kangaroo(0,3,4,2))