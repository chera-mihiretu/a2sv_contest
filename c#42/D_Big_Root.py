import sys

import threading

# take input
input = lambda: sys.stdin.readline().strip()
# solution
def solution():
    n = int(input())
    vals = [int(i) for i in input().split()]
    graph = [[] for _ in range(n)]
    parent = [int(i) for i in input().split()]
    for i in range(n - 1):
        graph[parent[i] - 1].append(i + 1)
    
    def rec(node):
        if not graph[node]:
            return vals[node]
        answer = float('inf')
        for i in graph[node]:
            back = rec(i)
            if back > vals[i]:
                answer = min(answer, (back + vals[i]) // 2)
            else:
                answer = min(answer, back)
        return answer
        
    print(rec(0) + vals[0])

        

def main():
    for i in range(int(input())):
        solution()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

