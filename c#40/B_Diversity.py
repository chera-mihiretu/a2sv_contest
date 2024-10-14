from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    k = int(input())
    if k > len(string):
        print('impossible')
    else:
        count = Counter(string)
        print(max(0, k - len(count)))

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()