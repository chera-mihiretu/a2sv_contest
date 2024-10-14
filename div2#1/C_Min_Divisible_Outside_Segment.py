from sys import stdin,stdout
from math import floor
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    q = int(input())
    answer = []
    for _ in range(q):
        l, r, d = [int(i) for i in input().split()]
        if not l <= d <= r:
            answer.append(d)
        else:
            right = floor(r / d) + 1
            answer.append(d * right)
    print(*answer, sep='\n')


    

# run the code
if __name__ == '__main__':
    test_case = 1#int(input())
    for i in range(test_case):
        solution()