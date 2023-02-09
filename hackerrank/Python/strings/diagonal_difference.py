def diagonalDifference(arr):
    a, b =0, 0
    for i in range(n):
        a += arr[i][i]
        b += arr[i][-(i+1)]
        
    return abs(a-b)


def diagonalDifference(arr):
    diag = [arr[i][i] - arr[n-1-i][i] for i in range(n)]
    return abs(sum(diag))