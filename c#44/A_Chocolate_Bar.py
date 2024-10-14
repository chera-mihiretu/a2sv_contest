from sys import stdin,stdout
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,l,r,k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    heap = []
    for i in range(n):
        if l <= nums[i] <= r:
            heap.append(nums[i])

    heapify(heap)
    count = 0
    answer = 0
    
    while heap:
        if heap[0] + count > k:
            break
        count += heappop(heap)
        answer += 1
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()