from sys import stdin,stdout
from collections import deque
from collections import defaultdict

# take input

input = lambda: stdin.readline().strip()
# solution
def solution():
    n, d, k = [int(i) for i in input().split()]

    police = [False for _ in range(n + 1)]

    police_places = [int(i) for i in input().split()]

    for i in police_places:
        police[i] = True
    graph = [[] for _ in range(n + 1)]
    mapp = defaultdict(int)
    for i in range(n -1):
        fr, to = [int(i) for i in input().split()]
        mapp[(fr, to)] = i + 1
        mapp[(to, fr)] = i + 1
        graph[fr].append(to)
        graph[to].append(fr)


    que = deque()
    visited = set()
    for i in range(n + 1):
        if police[i]:
            que.append((i, 0))
            visited.add(i)
    answer= set()
    while que:
        x = len(que)
        for i in range(x):
            node, cur_k =que.popleft()

            for child in graph[node]:
                if cur_k == k:
                    continue
                elif child in visited:
                    answer.add(mapp[(node, child)])
                else:
                    que.append((child, cur_k + 1))
                

    print(len(answer))
    print(*answer)
                    
        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()