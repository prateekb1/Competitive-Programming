# def minimumPlatform(self,n,arr,dep):
#         sorted_arr = sorted(arr + dep)
        
#         minPlatform = 0
#         trainsAtPlatform = 0
    
#         for i in sorted_arr:
#           if i in arr:
#             trainsAtPlatform += 1
#           if i in dep:
#             trainsAtPlatform -= 1
#           minPlatform = max(minPlatform, trainsAtPlatform)
        
#         return minPlatform

# def minimumPlatform(self,n,arr,dep):
#         platforms=0 
#         cmng=[]
#         gng=[]
#         for i in range(n):
#             gng.append(dep[i])
#             gng.sort()
#             if gng[0]>=arr[i] :
#                 platforms+=1
#             else:
#                 gng=gng[1:]
#         return platforms


def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        count =0
        ans = 0
        i,j = 0,0

        while (i<n):
            if arr[i] <= dep[j]:
                count += 1
                ans = max(ans,count)
                i += 1
            else:
                count -= 1
                j += 1
        return ans

print(minimumPlatform(6,[900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000
]))