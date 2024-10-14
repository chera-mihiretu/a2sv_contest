from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    string = input()
    count = 0
    for i in range(length - 1, -1, -1):
        if string[i] == ')':
            count += 1
        else:
            break
    if count > length // 2:
        print("Yes")
    else:
        print("No") 


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()