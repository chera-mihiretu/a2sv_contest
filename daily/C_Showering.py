from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, s, m = [int(i) for i in input().split()]
    task = [[0,0]]
    for _ in range(n):
        task.append([int(i) for i in input().split()])
    task.append([m, m])
    gap = 0
    for i in range(1, n + 2):
        gap = task[i][0] - task[i-1][1]
        if gap >= s:
            print("YES")
            return
    print("NO")


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()