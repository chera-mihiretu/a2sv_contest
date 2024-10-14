from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    aN, bN = [int(i) for i in input().split()]
    k,m = [int(i) for i in input().split()]
    A_nums  = [int(i) for i in input().split()]
    B_nums = [int(i) for i in input().split()]

    if A_nums[k-1] < B_nums[0]:
        print('YES') 
    else:
        print('NO')


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()