from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    l,r,k = [int(i) for i in input().split()]
    a,b = [int(i) for i in input().split()]


    if abs(l- r) < k:
        print(-1)
    else:

        

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()