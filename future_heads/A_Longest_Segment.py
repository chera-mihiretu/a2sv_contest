from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    curr = 1
    ans = 1
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            curr = 1
        else:
            curr += 1
        ans = max(ans, curr)
    print(ans)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()