from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b,k = [int(i) for i in input().split()]

    if k & 1:
        answer = (a - b ) * (k // 2) + a
    else:
        answer = (a - b ) * (k // 2) 
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()