def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    bcount = 0
    for i in range(len(apples)):
        temp = a + apples[i]
        if (temp in range(s,t)):
            acount += 1
    for k in range(len(oranges)):
        temp = b + oranges[k]
        if (temp in range(s,t)):
            bcount += 1
    print(acount)
    print(bcount)
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])