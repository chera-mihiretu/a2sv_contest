from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n  = int(input())
    nums = [int(i) for i in input().split()]

    answer = float('inf')
    answer_ind = [-1,-1]
    for i in range(len(nums)):
        if answer > abs(nums[i] - nums[i-1]):
            answer = abs(nums[i] - nums[i-1])
            answer_ind = [(i + 1), ((i-1) % n) + 1]
    print(*answer_ind)
# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()