from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    current = 1
    a_turn = False
    answer = [0, 0]
    while n != 0:
        if n > current:
            n -= current
        else:
            current = n
            n = 0
        if a_turn:
            answer[0] += current
            a_turn = False
        else:
            answer[1] += current
            a_turn = True
        current += 4
    print(*answer[::-1])


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()