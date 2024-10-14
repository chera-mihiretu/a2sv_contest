from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    prefix_left = [0, 0]
    prefix_right = [0,0]
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            prefix_left.append(prefix_left[-1] + nums[i-1] - nums[i])
        else:
            prefix_left.append(prefix_left[-1])
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            prefix_right.append(prefix_right[-1] + nums[i+1] - nums[i])
        else:
            prefix_right.append(prefix_right[-1])
    #print(prefix_left)
    #print(prefix_right)

    for _ in range(m):
        sj, tj = [int(i) for i in input().split()]
        if sj <= tj:
            print(prefix_left[tj] - prefix_left[sj])
        else:
            print(prefix_right[-tj] -prefix_right[-sj])



# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()