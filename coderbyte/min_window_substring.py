# from collections import Counter

# EMPTY_COUNTER = Counter()

# def MinWindowSubstring(strArr):
#   N, K = strArr
#   frequencyK = Counter(K)
#   options = []
#   for i in range(len(N)):
#     curr = Counter()
#     for j in range(i, len(N)):
#       curr[N[j]] += 1
#       if frequencyK - curr == EMPTY_COUNTER:
#         options.append(N[i:j + 1])
#         break
#   return min(options, key=len)


# METHOD 2
# def MinWindowSubstring(strArr):
#     if strArr[1] == '': return ''
        
#     t_dict, window = {}, {}
            
#     for c in strArr[1]:
#         t_dict[c] = 1 + t_dict.get(c, 0)
                
#     have, need = 0, len(t_dict)
#     res, resLen = [-1, -1], float('inf')
#     l = 0
            
#     for r in range(len(strArr[0])):
#         c = strArr[0][r]
#         window[c] = 1 + window.get(c, 0)
                
#         if c in t_dict and window[c] == t_dict[c]:
#             have += 1
                    
#         while have == need:
#             # update our result
#             if r - l + 1 < resLen:
#                 resLen = r - l + 1
#                 res = [l, r]
                        
#             # pop from left of window
#             window[strArr[0][l]] -= 1
#             if strArr[0][l] in t_dict and window[strArr[0][l]] < t_dict[strArr[0][l]]:
#                 have -= 1
                        
#             l += 1
                    
#     l, r = res
#     return strArr[0][l:r+1]


# METHOD 3
# def MinWindowSubstring(a):

#   x = len(a[1])
#   while True:
#     for i in range(x, len(a[0]) + 1):
#       y = a[0][i-x:i]
#       met = True
#       for z in set(list(a[1])):
#         if z not in y or y.count(z) < a[1].count(z):
#           met = False
#           break
#       if met == True:
#         return y
#     x += 1


# METHOD 4
def MinWindowSubstring(strArr):

  N, K = strArr[0], list(strArr[1])
  shortest = ""

  # Slide windows to get substrings
  for i in range(len(N)):
    for j in range(i, len(N)):
      sub = N[i:j+1]
      
      # Check if substring has all chars of K
      _K = K[:]
      for c in sub:
        if c in _K:
          _K.remove(c)
        if len(_K) == 0 and (shortest == "" or len(sub) < len(shortest)):
          shortest = sub

  # code goes here
  return shortest

print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))