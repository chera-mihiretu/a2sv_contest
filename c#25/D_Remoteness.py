
import sys, threading
# from collections import deque
input = lambda: sys.stdin.readline().strip()

def solution():
    n = int(input())
    graph = [[] for i in range(n)]
    for i in range(n):
        fr, to = [int(i) - 1 for i in input().split()]
        graph[fr].append(to)
        graph[to].append(fr)
    color = [0 for i in range(n)]
    def checkCycle(index, pre):
        if color[index] == 1:
            return index
        color[index] = 1
        for i in graph[index]:
            if i != pre:
                val = checkCycle(i, index)
                if val != -1:
                    return val
        color[index] = 2
        return -1
    where_cycle = checkCycle(0, -1)
    
    color = [0 for i in range(n)]

    checkCycle(where_cycle, -1)
    que = []
    for i in range(n):
        if color[i] == 0 or color[i] == 2:
            que.append(i)
    # print(graph)
    def another_helper(index, pre):
        if color[index] == 1:
            return 0
        val = float('inf')
        if answer[index] == 0 or answer[index] == float('inf'):
            for i in graph[index]:
                if i != pre:
                    val = min(another_helper(i, index) + 1, val)
            answer[index] = val
        return answer[index] 

    
    answer = [0 for i in range(n)]
    
    for i in que:
        answer[i] = another_helper(i, -1)
    print(*answer)
                
        
        


def solve():
    solution()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=solve)
    main_thread.start()
    main_thread.join()
