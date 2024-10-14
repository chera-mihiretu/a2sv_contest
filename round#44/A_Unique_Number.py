from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    count = Counter(nums)
    answer = float('inf')
    for item, freq in count.items():
        if freq == 1:
            answer = min(answer, item)
    if answer == float('inf'):
        return -1
    else:
        for i in range(n):
            if nums[i] == answer:
                return i + 1

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution())