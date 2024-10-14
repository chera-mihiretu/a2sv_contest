from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    print(nums[n//2])

# run the code
if __name__ == '__main__':
    test_case = 1#int(input())
    for i in range(test_case):
        solution()