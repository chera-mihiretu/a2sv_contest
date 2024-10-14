from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    """
        logva

        vo      agl
    """

    length = int(input())
    s = input()
    stack_one = []
    stack_two = []
    flag = True
    for i in range(len(s) - 1, -1, -1):
        if flag:
            stack_one.append(s[i])
            flag = False
        else:
            stack_two.append(s[i])
            flag = True
        one , two = ''.join(stack_two), ''.join(stack_one[::-1])
    print(one + two)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()