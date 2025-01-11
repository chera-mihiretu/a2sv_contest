from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, m = [int(i) for i in input().split()]
    nums_top  = [int(i) for i in input().split()]
    nums_bottom = [int(i) for i in input().split()]

    nums_bottom.sort()
   
    bottom_point = 0
    contian = set(nums_top)

    for i in range(n - 1, -1, -1):
        if nums_top[i] == 0:
            while bottom_point < m and nums_bottom[bottom_point] in contian:
                bottom_point += 1
            if  bottom_point < m:
                nums_top[i] = nums_bottom[bottom_point]
            bottom_point += 1
    right = False
    # print(nums_top)
    for i in range(1, n):
        if nums_top[i] < nums_top[i-1]:
            right = True
        if nums_top[i] == 0:
            right = False
            break
    if right:
        print('Yes')
    else:
        print("No")
            

    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()