from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    length = int(input())
    string = input()

    my_s = list(string)
    pointer = 0
    for i in range(len(my_s)):
        while pointer < len(my_s) and my_s[pointer] == 'b':
            pointer += 1
        if i > pointer:
            if my_s[i] == 'b':
                my_s[i], my_s[pointer] =  my_s[pointer], my_s[i]
                pointer += 1
    print(''.join(my_s))

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()