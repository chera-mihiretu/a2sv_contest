from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m,k = map(int,input().split())

    if min(m,k) < n:
        print('No')
    else:   
        print("Yes")

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()