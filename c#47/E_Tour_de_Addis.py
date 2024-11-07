from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    graph = [[] for i in range(n + 1)]
    for _ in range(m):
        fr, to, we = [int(i) for i in input().split()]
        graph[fr].append([to, we])
    slowness = [int(i) for i in input().split()]
    
    distance = [float('inf') for i in range(n + 1)]
    distance[1] = 0
    Visited = [False for i in range(n + 1)]

    heap = [(0, 1)]
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()