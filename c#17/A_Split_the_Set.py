from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    odd  = even = 0
    for i in range(len(nums)):
        if nums[i] & 1: 
            odd += 1
        else:
            even += 1
    if odd != even: 
        print("No")
    else:
        print("Yes")
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()