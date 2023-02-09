def zigzag(arr):
    for i in range(1,len(arr)):
        if i % 2 == 0 and arr[i-1] < arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
        elif i % 2 == 1 and arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
    print(arr)

if __name__== "__main__":
    arr = [4,3,7,8,6,2,1] # 4 7 3 
    n = len(arr)
    zigzag(arr)