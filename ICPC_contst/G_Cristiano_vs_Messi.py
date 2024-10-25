# Blank (2Sami, Chera)

from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():



    nums = [int(i) for i in input().split()]
    nums.sort()
    if not (nums[0] + nums[1] == nums[2]):
        return False
    return True
        

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        if solution():
            print('YES')
        else:
            print('NO')