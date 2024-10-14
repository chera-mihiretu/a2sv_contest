from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    burles = int(input())
    
    dp = [float('inf') for _ in range(burles + 1)]

    dp[0] = 0

    for i in range(burles + 1):
        if i + 1 < burles + 1:
            dp[i+1] = min(dp[i+1], dp[i]+1)
        if i + 3 < burles + 1:
            dp[i+3] = min(dp[i], dp[i+3])
        if i + 5 < burles + 1:
            dp[i+5] = min(dp[i], dp[i+5])
    return dp[burles]

    


    
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(solution())