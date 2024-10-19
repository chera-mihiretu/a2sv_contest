from sys import stdin,stdout
from math import gcd
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    essense = int(input())

    water = 100 - essense

    for i in range(2,  101):
        
        while (water % i) == 0 and (essense % i == 0):
            water //= i
            essense //= i
    print(water + essense)



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()