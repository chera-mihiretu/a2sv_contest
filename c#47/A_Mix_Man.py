from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums1 = [int(i) for i in input().split()]
    nums2 = [int(i) for i in input().split()]

    for i in range(n):
        if nums1[i] < nums2[i]:
            nums1[i], nums2[i] = nums2[i], nums1[i]
    answer = max(nums1) * max(nums2)

    print(answer)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()