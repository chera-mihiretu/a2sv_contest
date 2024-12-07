from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    if n % 2 == 0:
        print('NO')
    else:
        print("YES")

        answer_one = []
        answer_two = []
        for i in range(1, 2 * n + 1):
            if i & 1:
                answer_one.append(i)
            else:
                answer_two.append(i)
        for i in range(0, n, 2):
            answer_one[i], answer_two[i] = answer_two[i], answer_one[i] 
        print(*answer_one, *answer_two)

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()