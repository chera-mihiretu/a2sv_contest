
import sys, threading
from collections import deque
input = lambda: sys.stdin.readline().strip()
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    graph = [[] for _ in range(n + 1)]
    degree = [0 for _ in range(n+1)]

    for i in range(n - 1):
        graph[i+2].append(nums[i]) 
        degree[nums[i]] += 1
    que = deque()
    print(graph)
    for i in range(1, n + 1):
        if degree[i] == 0:
            que.append(i)
    result = 0
    while que:
        x = len(que)
        result += x // 2
        for i in range(x):
            node = que.pop()
            for i in graph[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    que.append(i)
    print(result)




    

    
def main():
    test = int(input())
    for _ in range(test):
        solution()
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
