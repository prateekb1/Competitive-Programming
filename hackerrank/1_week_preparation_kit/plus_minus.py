def plusMinus(arr):
    # Write your code here
    posi = 0
    negi = 0
    zero = 0
    for i in arr:
        if i > 0:
            posi += 1
        elif i < 0:
            negi += 1
        else:
            zero += 1
    print( posi/len(arr) )
    print( negi/len(arr) )
    print( zero/len(arr) )

