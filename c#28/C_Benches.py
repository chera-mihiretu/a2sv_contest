from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    m = int(input())
    arr= []
    total = 0
    max_num = 0
    for i in range(n):
        arr.append(int(input()))
        total += arr[i]
        max_num = max(max_num, arr[i])

    max_pos = max_num * n

    rem = max_pos - total
    hold = max(0, m - rem)

    hold = ceil(hold / n)

    min_k = max_num + hold

    max_k = max_num + m
   

    print(min_k, max_k)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()