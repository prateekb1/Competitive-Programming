def countingSort(arr):
    # Write your code here
    new = [0 for i in range(100)]
    for i in arr:
            new[i] += 1
    return new

print(countingSort([1,2,3,3,4,5,3,6,6,7,3,6,2,6,2,4,2,6,4]))