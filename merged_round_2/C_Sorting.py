from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    nums = [int(i) for i in input().split()]

    start = 0

    end = n - 1

    while (start  + 1) < n and nums[start] <= nums[start + 1]:
        start += 1

    while (end  - 1) >= 0 and nums[end] >= nums[end - 1]:
        end -= 1

    if end < start:
        print("yes")
        print(1, 1)
        return 
    else:
        t_start, t_end = start , end 
        while t_start < t_end:
            nums[t_start], nums[t_end] = nums[t_end], nums[t_start]
            t_start += 1
            t_end -= 1
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            print("no")
            return
    print("yes")
    print(start + 1, end + 1)

    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()