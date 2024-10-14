from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        fr, to = [int(i)  for i in input().split()]
        graph[fr].append(to)
        graph[to].append(fr)
    answer = list(zip(range(n+1), graph))
    answer.sort(key=lambda x: len(x[1]), reverse=True)

    print(answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()