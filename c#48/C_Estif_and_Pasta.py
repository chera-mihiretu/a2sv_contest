from sys import stdin,stdout
from math import perm, comb
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    MOD = pow(10, 9) + 7
    k = int(input())

    number_of_nodes = (pow(2, k)) - 1

    answer = 6 * pow(4, (number_of_nodes-1), MOD) 
    


    print(answer % MOD)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()