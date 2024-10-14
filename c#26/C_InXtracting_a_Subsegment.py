from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    if k == 1:
        print(min(nums))
    elif k == 2:
        print(max(nums[0], nums[-1]))
    else:
        print(max(nums))

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()