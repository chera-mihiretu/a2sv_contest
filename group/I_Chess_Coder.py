from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    if n % 2 == 0:
        ans = n
    matrix = [["."]*n for _ in range(n)]
    ct = 0
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0 or matrix[i][j-1] == '.':
                    matrix[i][j] ="C"
                    ct += 1
            else:
                if matrix[i-1][j] == ".":
                    matrix[i][j] = "C"
                    ct += 1
    print(ct)
    for row in matrix:
        print("".join(row))

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    # for i in range(test_case):
    solution()