from sys import stdin,stdout
from math import factorial
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    count = Counter(nums)

    print(factorial(len(count)))

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()