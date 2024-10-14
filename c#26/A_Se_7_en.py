from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    number = int(input())
    if number % 7 == 0:
        print(number)
    else:
        dev = number // 7
        ans_1 = dev * 7
        ans_2 = (dev + 1) * 7

        num = str(number)
        ans_1 = str(ans_1)
        ans_2 = str(ans_2)
        if len(num) == len(ans_1) and len(num) == len(ans_2):
            count  = 0
            for i in range(len(num)):
                if num[i] != ans_1[i]:
                    count += 1
            if count == 1:
                print(ans_1)
            else:
                print(ans_2)
        elif len(num) == len(ans_1):
            print(ans_1)
        else:
            print(ans_2)
        
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()