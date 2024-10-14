from sys import stdin,stdout
from collections import deque
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    with_indx = list(zip(nums, list(range(n))))
    #print(with_indx)
    line = deque(with_indx)
    while len(line) > 1:
        take, indx = line.popleft()
        take -= m
        if take > 0:
            line.append((take, indx))
    print(line[0][1] + 1) 
# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()