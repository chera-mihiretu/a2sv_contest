
import sys, threading

input = lambda: sys.stdin.readline().strip()


def solution():
    n, h = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    nums.sort()
    def rec(index, green, blue, h):
        if index == n:
            return 0
        blue_used = 0
        green_used = 0
        if h > nums[index]:
            return rec(index + 1, green, blue, h + nums[index] // 2) + 1
        if blue:
            blue_used = rec(index, green, blue - 1, h * 3) 
        if green:
            green_used = rec(index, green - 1, blue, h * 2) 
        

        return max(green_used, blue_used)
    print(rec(0, 2, 1, h))
        



def main():
    for _ in range(int(input())):
        solution()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
