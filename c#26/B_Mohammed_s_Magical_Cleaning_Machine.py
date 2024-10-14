from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    start, end = 0, 0
    answer = 0
    while start <= length - 2:
#        print(nums)

        while end < length - 1 and nums[end]:
            end += 1
        if end == length -1:
            answer += nums[start]
            nums[end] += nums[start]
            start += 1
        else:
            if nums[start] == 0:
                if start == end:
                    end += 1
                start += 1
                
            else:
                answer += 1
                nums[end] += 1
                nums[start] -= 1
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()