import sys

import threading

# take input
input = lambda: sys.stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    memo = {}
    def helper(index, devider):

        if index == n:
            return 0
        if (index, devider) not in memo:
            half = helper(index + 1, devider * 2) + (nums[index] // devider)
            full = helper(index + 1, devider) + ((nums[index] // (devider // 2)) - k)
            memo[(index, devider)] = max(half, full)
        
        return memo[(index, devider)]
    print(helper(0, 2))
        

def main():
    for i in range(int(input())):
        solution()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

