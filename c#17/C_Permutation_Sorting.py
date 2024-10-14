from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    index = {c : i for i, c in enumerate(nums)}
    pre = -1
    res = 0
    for i in range(1, n + 1):
        if index[i] > pre:
            pre = index[i]
        else:
            res += 1
            pre = index[i]
    print(res)



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()
