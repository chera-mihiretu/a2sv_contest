from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a = int(input())
    b = int(input())

    diff = abs(a - b)

    a_move = 1
    b_move = 1
    answer = 0
    while diff:
        # print(a, b)
        if a_move <= b_move:
            diff -= 1
            answer += a_move
            a_move += 1
        else:
            diff -= 1
            answer += b_move
            b_move += 1
    print( answer)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()