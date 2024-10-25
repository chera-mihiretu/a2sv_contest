# Blank (2Sami, Chera)
from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    answer = []
    for i in range(len(string)):
        if string[i] != '0':
            cur_ans = string[i] + ('0' * (len(string) - i - 1))
            answer.append(cur_ans)
    print(len(answer))
    print(*answer)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()