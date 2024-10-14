from sys import stdin 

input = lambda: stdin.readline().strip()

def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    start, end = 0, len(nums) - 1
    answer = []
    while start < end:
        if start == end:
            answer.append(nums[start])
            end -= 1
            start += 1
        else:
            answer.append(nums[end])
            answer.append(nums[start])
            start += 1
            end -= 1
    for i in range(1, n):
        if i & 1:
            if nums[i] > nums[i-1]:
                print("Impossible")
                return
            elif nums[i] < nums[i-1]:
                print("Impossible")
                return
    print(*answer)

if __name__ == '__main__':
    solution()
