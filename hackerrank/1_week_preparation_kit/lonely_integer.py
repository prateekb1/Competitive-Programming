# a = [1,2,3,4,3,2,1]
# The unique element is 4
# import collections
def lonelyinteger(a):
    # Write your code here
    # Performance Solution
    # return " ".join(str(val) for val,count in
    # collections.Counter(a).items() if count == 1)

    # XORing two equal numbers cancels them out. XOR all numbers together.
    answer = 0
    for i in a:
        answer ^= i
    return answer

    # METHOD 1
    # for val in a:
    #     if a.count(val) == 1:
    #         return val

    # METHOD 2
    # result = [ val for val in a if a.count(val)==1 ]
    # return result[0]

print(lonelyinteger([1,2,3,4,3,2,1]))