from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    nums = [int(i) for i in list(input())]
    # print(nums)
    answer = [0 for i in range(n)]
    answer[0] = nums[0] + 1
    res = [0 for i in range(n)]
    res[0] = 1
    for i in range(1, n):
        answer[i] = nums[i] + 1
        res[i] = 1
        if answer[i] == answer[i-1]:
            answer[i] -= 1
            res[i] -= 1
    print(*res, sep='')

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()