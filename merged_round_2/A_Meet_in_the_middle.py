from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    x, y, a, b = [int(i) for i in input().split()]

    result = (y - x ) / (a + b)

    if result == int(result):
        print(int(result))
    else:
        print(-1)



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()