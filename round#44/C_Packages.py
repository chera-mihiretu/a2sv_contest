from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]

    start = 1
    end = k
    while start <= end:
        mid = start + (end - start) // 2
        
        



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()