from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    twos = []
    for i in range(1, 30):
        twos.append(2 ** i)
    twos_set = set(twos)
    nums_set = set(nums)
    answer = set()
    for i in range(len(nums)):
        cur_set = set()
        cur_set.add(nums[i])
        for j in range(len(twos)):
            cur_set.add(nums[i] - twos[j])
            cur_set.add(nums[i] + twos[j])
        
        cur_ans = cur_set & nums_set
        if len(cur_ans) > len(answer):
            answer = cur_ans
    if len(answer) == 1:
        for i in nums:
            if abs(i) in twos:
                print(1)
                print(i)
                return
    
    print(len(answer))
    for i in answer:
        print(i, end=' ')
        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()