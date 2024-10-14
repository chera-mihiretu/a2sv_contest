from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b,c,d = [int(i) for i in input().split()]

    if min(a, b) > max(c, d):
        print(4)
        return
    if min(c, d) >= max(a, b):
        print(0)
        return
    print(2)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()