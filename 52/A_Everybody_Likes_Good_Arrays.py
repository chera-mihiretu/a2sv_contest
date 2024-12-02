from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    count = 0
    n = int(input())
    nums = [int(i) for i in input().split()]
    for i in range(1, len(nums)):
        # print(nums[i] & 1, nums[i-1] & 1)
        if (nums[i] & 1) == (nums[i-1] & 1):
            count += 1
    print(count)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()