from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    graph = [[] for i in range(n + 1)]
    disrespectors = set()
    for i in range(1, n + 1):
        pi, ci = [int(i) for i in input().split()]
        if pi == -1:
            continue
        if ci == 1:
            disrespectors.add(i)
        graph[pi].append(i)
    answer = []
    for i in disrespectors:
        has = True
        for j in graph[i]:
            if j not in disrespectors:
                has  = False
        if has:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        print(-1)
    else:
        print(*answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()