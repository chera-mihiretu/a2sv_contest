
import sys, threading
from collections import defaultdict
from math import ceil
input = lambda: sys.stdin.readline().strip()
def solution():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    nums = [int(i) for i in input().split()]
    for i in range(n - 1):
        graph[nums[i]].append(i + 2)
        graph[i + 2].append(nums[i])

    childs_of_same_parent = defaultdict(list)
    def set_parent(index, prev):
        for i in graph[index]:
            if i != prev:
                childs_of_same_parent[index].append(i)
                set_parent(i, index)
    set_parent(1, 0)
    another_graph = list(childs_of_same_parent.values())
   
    another_graph.sort(reverse=True, key = lambda x: len(x))


    answer = len(another_graph) + 1
    left = 0
    
    for i in range(len(another_graph)):
        left += max(0, len(another_graph[i]) - (len(another_graph) - i))


    answer += ceil(left / 2)
    print(answer)
    
    

        

def solve():
    t =  int(input())
    for i in range(t):
        solution()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=solve)
    main_thread.start()
    main_thread.join()
