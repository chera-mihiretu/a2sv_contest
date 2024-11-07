from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    MOD = pow(10, 9) + 7
    x, y = [int(i) for i in input().split()]
    i = int(input()) 
    nums = []
    if x != y:
        nums = [x, y]

        while nums[-1] != nums[0]:
            nums.append(nums[-1] - nums[-2])
        
        
        nums.pop()
    else:
        nums = [x, y, 0, -x, -x, 0]

    index = i % len(nums)

    answer = nums[index - 1]
    print(answer % MOD)



# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()