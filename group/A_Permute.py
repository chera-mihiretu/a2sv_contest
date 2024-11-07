from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    for i in range(n):
        if nums[i] != (i + 1):
            break
    else:
        return 0

    if nums[0] == 1:
        return 1
    if nums[-1] == n:
        return 1
    if nums[0] == n and nums[-1] == 1:
        return 3
    return 2
        
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution())