from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    count = Counter(nums)
    answer = 0
    for num, freq in count.items():
        if freq == 1:
            answer += 1
        elif freq > 1:
            if (-num) not in count:
                answer += 2
            else:
                answer += 1
    print(answer) 
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()