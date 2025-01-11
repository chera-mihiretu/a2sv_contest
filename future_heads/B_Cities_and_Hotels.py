from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, d = [int(i) for i in input().split()]

    arr = [int(i) for i in input().split()]
    arr.sort()
    answer = 0
    for i in range(1, n ):
        start = arr[i-1] + d
        end = arr[i] - d
        # print(start, end)

        curr = max(0, end - start + 1)

        answer += min(2, curr)
    print(answer + 2)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()