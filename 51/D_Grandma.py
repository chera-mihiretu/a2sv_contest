from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    s = input()
    content = set(list(s))
    answer = float('inf')
    for char in content:
        start = 0
        end = len(s) - 1
        possible = 0
        count = 0
        while start < end:
            possible = True
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if s[start] == char:
                    start += 1
                elif s[end] == char:
                    end -= 1
                else:
                    possible = False
                    break
                count += 1
        if possible:
            answer = min(answer, count)
    print(answer if answer != float('inf') else -1)


# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()