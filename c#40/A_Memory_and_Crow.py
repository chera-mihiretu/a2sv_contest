from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    pref = []
    for i in range(len(nums) -1):
        pref.append(nums[i] + nums[i+1])
    pref.append(nums[-1])
    print(*pref)


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()