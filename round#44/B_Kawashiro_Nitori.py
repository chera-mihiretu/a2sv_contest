from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,k = [int(i) for i in input().split()]
    string = input()

    count = Counter(string)

    if k ==0:
        return 'YES'
    else:
        pass


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()