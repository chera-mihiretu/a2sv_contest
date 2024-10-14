from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    grid = []
    
    for _ in range(n):
        grid.append([int(i) for i in input().split()])
    if n == 1:
        print('YES')
        print(7)
        return
    answer= [-1 for i in range(n)]
    for i in range(n):
        ands = -1
        for j in range(n):
            if i == j:
                continue
            if ands == -1:
                ands = grid[i][j]
            else:
                ands &= grid[i][j]
        answer[i] = ands
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if answer[i] | answer[j] != grid[i][j]:
                print('NO')
                return
    print('YES')
    print(*answer)




# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()