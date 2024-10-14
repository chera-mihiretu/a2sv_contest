from sys import stdin,stdout
from collections import deque
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple((int(i) for i in input().split())))

    dirs = [[1,0], [0,1], [-1, 0], [0, -1], [1,1], [-1,-1]]
    
    answer = []
    
    points_set = set(points)
    for i in range(n):
        visited = set()
        que = deque()
        que.append(points[i])
        length = 0
        while True:
            x = len(que)
            length += 1
            for i in range(x):
                fr, to = que.popleft()
                for x, y in dirs:
                    if (fr + x, to + y) not in points_set:
                        answer.append([fr + x, to + y])
                        break
                    else:
                        if (fr + x, to + y) not in visited:
                            visited.add((fr + x, to + y))
                            que.append([fr + x, to + y])
                else:
                    continue
                break
            else:
                continue
            break
    for i in answer:
        print(*i)





# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()