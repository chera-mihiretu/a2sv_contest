from sys import stdin,stdout
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    heap = []
    for _ in range(n):
        a, b = [int(i) for i in input().split()]

        heap.append([-b,-a])
    counter = 1
    answer = 0
    heapify(heap)
    while counter:
        
        counter -= 1
        if not heap:
            break
        repeat, point = heappop(heap)

        answer += -point
        if repeat:
            counter += -repeat

    print(answer)

        

# run the code
if __name__ == '__main__':
    test_case = 1#int(input())
    for i in range(test_case):
        solution()