from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    candy = int(input())

    def calc(candy, mid):
        a, b = 0, 0
        turn = True
        while candy:
            if turn:
                a += min(candy, mid) 
                candy = max(0, candy - mid)
                turn = False
            else:
                b += candy // 10
                candy -= candy // 10
                turn = True
        return a >= b

    start, end = 1, candy
    answer = -1
    while start <= end:
        mid = start + (end - start) // 2
        ans = calc(candy,  mid)
        if ans:
            #print(mid)
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    print(answer)


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()