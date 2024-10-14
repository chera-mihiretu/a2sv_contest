from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    if n == 1:
        print(0)
        return
    nums.sort()
    diffs = []
    for i in range(1, n):
        diffs.append(nums[i] - nums[i-1])
    
    thre_max = list(zip(diffs, list(range(len(diffs)))))
    thre_max.sort(reverse=True)
    
    first = thre_max[0][1] + 1
    second = thre_max[1][1] + 1


    first_sum = ceil(sum(nums[0 : first]) / first)
    second_sum = ceil(sum(nums[first : second]) / (second - first)) 
    third_sum = ceil(sum(nums[second : len(nums)]) / (len(nums) - second))

    answer = 0
    for i in range(n):
        if i < first:
            answer = max(abs(first_sum - nums[i]), answer)
        elif i >= first > second:
            answer = max(abs(second_sum - nums[i]), answer)
        else:
            answer = max(abs(third_sum - nums[i]), answer)
    print(answer)




    


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()