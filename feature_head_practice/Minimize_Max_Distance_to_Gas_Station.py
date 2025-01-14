from typing import * 

class Solution:
    def findSmallestMaxDist(self, stations, k):
        def check(m):
            cnt = 0
            for i in range(1, len(stations)):
                cnt += int((stations[i] - stations[i-1]) / m)
            return cnt <= k
            
            
        left, right = 0, 1e8
        
        while right - left > 1e-6:
            
            mid = (right + left) / 2
         
            if check(mid):
                right = mid
            else:
                left = mid
        return left 

nums = eval(input())
k = int(input())

s = Solution()
print(s.findSmallestMaxDist(nums, k))

