from sys import stdin 

input = lambda: stdin.readline().strip()

def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    start, end = 0, len(nums) - 1
    answer = []
    #print(nums)
    while start <= end:
        if start == end:
            answer.append(nums[start])
            end -= 1
            start += 1
        else:
            answer.append(nums[start])
            answer.append(nums[end])
            start += 1
            end -= 1
    
    print(*answer)

if __name__ == '__main__':
    solution()
