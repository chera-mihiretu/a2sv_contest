from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,k = [int(i) for i in input().split()]
    my_k = 0
    k_m1 = 0
    k_p1 = 0
    for i in range(n):
        start, end = [int(i) for i in input().split()]
        if start <= k <= end:
            my_k += 1
            if start <= k - 1 <= end:
                k_m1 += 1
            if start <= k + 1 <= end:
                k_p1 += 1

    if my_k == k_m1 or my_k == k_p1:
        print("NO")
    else:
        print('YES')



# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()