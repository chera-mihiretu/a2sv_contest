
import sys, threading

input = lambda: sys.stdin.readline().strip()

memo = {}
def solution():



    t = int(input())
    for i in range(t):
        n = int(input())
        answer = main(n)
        print(answer if answer != float('inf') else -1)



def main(n):
    if n > 45:
        return float('inf')
    answer = float('inf')
    def rev(number):
        return int(str(number)[::-1])
    if n not in memo:
        def recursion(number, total, start):
            nonlocal answer
            if total >= n:

                if total == n:
                    reverted = rev(number)
                    answer = min(answer, number)
                return 
            for i in range(start + 1, 9 + 1):
                recursion(number * 10 + i,  total + i, i)
    
        recursion(0, 0, 0)
        memo[n] = answer
    return memo[n] if memo[n] != float('inf') else -1
    
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=solution)
    main_thread.start()
    main_thread.join()
