from sys import stdin,stdout
from math import lcm
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b = [int(i) for i in input().split()]
    c,d = [int(i) for i in input().split()]


    sub = max(a, b) - min(a, b)
    
    print(lcm(sub, sub // 9))


        




        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        print(solution())