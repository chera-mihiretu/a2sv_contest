from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]


    total = sum(nums)
    answer = float('inf')
    if total & 1:
        for num in nums:
            count = 0
            curr = num 
            hold_total = total
            while hold_total  & 1:
                hold_total -= ceil(curr / 2)
                curr = curr // 2
                count += 1
            answer = min(answer, count)

    if answer == float('inf'):
        print(0)
    else:
        print(answer)
    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()