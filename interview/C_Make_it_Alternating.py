from sys import stdin,stdout
from math import factorial
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    n = len(string)
    k = 1
    count = 1
    comm = []
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            k += 1
            comm.append(count)
            count = 1  
    answer = factorial(n-k)
    for i in comm:
        answer *= i 
    
    print(n - k,  answer)     
    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()