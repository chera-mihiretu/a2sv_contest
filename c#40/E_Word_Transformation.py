from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string, expected = input().split()
    p_2 = len(expected) - 1
    contain = set()
    for p_1 in range(len(string)-1, -1, -1):
        
        if p_2 >= 0 and expected[p_2] == string[p_1]:
            if string[p_1] in contain:
                print('NO')
                return

            p_2 -=1
        else:
            contain.add(string[p_1])
    if p_2 >= 0:
        print('NO')
    else:
        print('YES')


            




# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()