from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    nums.sort()
    number = 1
    for i in range(n):
        if nums[i] >= number:
            nums[i] = number
            number += 1
    number = 1
    for i in range(n):
        if nums[i] == number:
            number += 1
    print(number)
    




# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()