from typing import * 
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        answer = 0
        stack = []
        nums.append(float('-inf'))

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()

                answer += i - index 
            stack.append(i)


        return answer
        





nums = eval(input())

ob = Solution()

print(ob.validSubarrays(nums))