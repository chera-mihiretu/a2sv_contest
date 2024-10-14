from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    start = [int(i) for i in input().split()]
    second = [int(i) for i in input().split()]
    third = [int(i) for i in input().split()]

    count_start = Counter(start)
    count_second = Counter(second)
    count_third = Counter(third)
    answer = []
    for num, times in count_start.items():
        if times != count_second[num]:
            answer.append(num)
    for num, times in count_second.items():
        if times != count_third[num]:
            answer.append(num)
    print(*answer, sep='\n')


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()