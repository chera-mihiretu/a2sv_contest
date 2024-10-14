from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    grid = []
    row_content = []
    for _ in range(n):
        grid.append([int(i) for i in input().split()])
        row_content.append(set(grid[-1]))
    #print(row_content)
    #print(grid)
    for i in range(n):
        for j in range(n):
            #print(grid[i][j])
            if grid[i][j] == 1:
                continue
            for k in range(n):
                #print(grid[i][j], grid[k][j])
                if k != i:
                    if (grid[i][j] - grid[k][j]) in row_content[i]:
                        break
            else:
                return False
    return True
    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        if(solution()):
            print('Yes')
        else:
            print('No')