from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    l,r,k = [int(i) for i in input().split()]
    a,b = [int(i) for i in input().split()]

    
    a, b = min(a,b), max(a,b)
    
    if a == b:
        return 0
    if (r  - l < k) or (abs(a - l) < k  and abs(r - a) < k) or (abs(b - l) < k  and abs(r - b) < k):
        return -1
    elif b - a >= k:
        return 1
    elif b - a < k and a - l >= k or r - b >= k:
        return 2
    return 3

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution())