from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    count = Counter(nums)

    print(max(count.values()))

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()