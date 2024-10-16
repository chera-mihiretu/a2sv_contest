from sys import stdin,stdout
from math import comb
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    string = input()
    count = 1
    removes = 0
    fromNumber = 0
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            
            removes += count - 1
            fromNumber += count if count != 1 else 0
            count = 1
    if count != 1:
        removes += count - 1
        fromNumber += count
    
    answer =   comb(fromNumber, removes)
    
    number = string.count('0')
    print(removes, answer *( 2 if number == 0 or number - len(string) == 0 else 1))



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()