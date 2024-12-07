from sys import stdin,stdout
from heapq import *

# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m, k = [int(i)  for i in input().split()]
    graph = [[] for i in range(n)]
    distance = [float('inf') for i in range(n)]
    processed = [False for i in range(n)]
    pathes = set()
    children = {}
    count = 0
    for _ in range(m):
        fr, to, weight = [int(i) -1 for i in input().split()]
        graph[fr].append((to, weight + 1))
        graph[to].append((fr, weight + 1))
        count += 1
    for _ in range(k):
        to, weight = [int(i) - 1 for i in input().split()]
        graph[0].append((to, weight + 1))
        count += 1
    heap = [[0,0]]
    while heap:
        cur_distance, node = heappop(heap)
        if not processed[node]:
            processed[node] = True
            for child, weight in graph[node]:
                if cur_distance + weight < distance[child]:
                    if child in children:
                        pathes.discard((children[child], child))
                    children[child] = node
                    pathes.add((node, child))
                    distance[child] = cur_distance + weight
                    heappush(heap, [distance[child], child])
    answer = list(pathes)
    print(pathes)
    for fr, to in answer:
        if (fr, to) in pathes:
            pathes.discard((to, fr))
    print(len(pathes))
    

        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()