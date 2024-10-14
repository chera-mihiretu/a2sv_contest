from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    nums =[int(i) for i in input().split()]

    mini, maxi = 0,0
    for i in range(n):
        if nums[mini] > nums[i]:
            mini = i
        if nums[maxi] < nums[i]:
            maxi = i
    print(mini + 1, maxi + 1)
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()