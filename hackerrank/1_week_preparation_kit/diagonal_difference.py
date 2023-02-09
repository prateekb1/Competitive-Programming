# Given a square matrix, calculate the absolute difference between the sums of its diagonals. For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
#

def diagonalDifference(arr):
    # Write your code here
    prim =0
    sec=0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(prim-sec)

print(diagonalDifference([[1,2,3],[4,5,6],[9,8,7]]))