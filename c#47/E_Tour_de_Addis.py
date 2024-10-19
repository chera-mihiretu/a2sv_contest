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
    print(graph)
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()