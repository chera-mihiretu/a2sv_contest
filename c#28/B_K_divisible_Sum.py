from sys import stdin,stdout
from math import ceil
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]

    times = ceil(n/k)

    k = k * times


    print(ceil(k / n))


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()