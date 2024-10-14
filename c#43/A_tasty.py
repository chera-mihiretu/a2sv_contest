from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    candies, people = [int(i) for i in input().split()]

    fair = candies // people


    remain = candies % people
    answer = [0 for i in range(people)]
    for i in range(people-1, -1, -1):
        answer[i] = fair + min(1, remain)
        if remain !=0:
            remain -= 1
    print(*answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()