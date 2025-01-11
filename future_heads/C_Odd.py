from sys import stdin,stdout
from collections import Counter
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    arr = [int(i) for i in input().split()]

    mmap = Counter()

    arr.sort(reverse=True)
    heap = []
    ans = 0
    for i in arr:
        if i % 2 == 0 and i not in mmap:
            heappush(heap, -i)
            mmap[i] = 1
    heapify(heap)
    while heap:
        top  = -heappop(heap)

        if top in mmap:
            div = top // 2

            if div % 2 == 0 and div not in mmap:
                heappush(heap, -div)
                mmap[div] = 1
            mmap.pop(top)
            ans +=1
    print(ans)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()