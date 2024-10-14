from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    
    n = int(input())
    rem = n // 10
    n = n % 10

    print(n + rem)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()