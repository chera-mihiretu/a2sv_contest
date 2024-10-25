from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    lst = [int(i) for i in input().split()]

    a = lst[0]

    lst.sort()
    print(3 - lst.index(a))


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()