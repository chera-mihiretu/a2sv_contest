
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = [int(i) for i in input().split()]
    answer = -1
    memo = set()
    def rec(total, twos, ones):
        nonlocal answer, memo
        
        if answer != -1:
            return -1
        if total >= n:
            if (twos + ones) % m == 0:
                answer = (twos +  ones)
            return -1
        
        if (twos, ones) not in memo:
            rec(total + 2, twos + 1, ones)
            rec(total + 1, twos, ones + 1)
        memo.add((twos, ones))
        
    rec(0, 0, 0)
            

    print(answer)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
