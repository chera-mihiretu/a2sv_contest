from sys import stdin,stdout
from math import comb
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())

    answer = comb(n, 7) + comb(n, 6) + comb(n, 5)
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()