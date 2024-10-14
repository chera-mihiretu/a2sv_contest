from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    count = 0

    answer = True
    while answer:
        if not n & 1:
            n = n // 2
            count += 1
            continue
        if (n * 2) % 3 == 0:
            n = (n * 2) // 3
            count += 1
            continue
        if (n * 4) % 5 == 0:
            n = (n * 4) // 5
            count += 1
            continue
        answer = False

    if n == 1:
        print(count)
    else:
        print(-1)


        
        

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()