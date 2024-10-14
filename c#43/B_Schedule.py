from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    nums = [int(i) for i in input().split()]

    there = True if nums[0] == 1 else False
    answer = 0 if not there else 1
    if n == 1:
        print(answer)
        return 
    for i in range(1, n):
        if nums[i] == 0:
            
            if nums[i-1] == 0:
                if there:
                    answer -= 1
                there = False
            else:
                answer += 1
        else:
            answer +=1 
            there = True
    if nums[i] == 0:
        if there:
            answer -= 1
    print(answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()