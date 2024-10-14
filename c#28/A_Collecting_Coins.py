from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b,c,k = [int(i) for i in input().split()]
    total = sum([a, b, c, k])
    n = 0
    if total % 3 != 0:
        print("NO")
    else:
        div = total // 3
        for i in [a,b,c]:
            if div < i:
                print("NO")
        print("YES")
    



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()