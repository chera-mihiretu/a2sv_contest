from sys import stdin,stdout
from heapq import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, s = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    
    start = 1
    end = n 

    def do_the_work(k):
        temp = []
        for i in range(n):
            temp.append(nums[i] + (i+1)*k)
        temp.sort()
        total = sum(temp[:k])
        return total <= s, total


    b_ans = 0
    
    while start <= end:
        mid = start + (end - start) // 2
        is_true, ss = do_the_work(mid)

        if is_true:
            b_ans = ss
            start = mid + 1
        else:
            end = mid - 1


    print(end, b_ans)
            

        



    

        
    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()