from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, x, m = [int(i) for i in input().split()]
    my_range = [x, x]
    for _ in range(m):
        #print(my_range)
        start, end = [int(i) for i in input().split()]
        if my_range[0] <= start <= my_range[1] or my_range[0] <= end <= my_range[1]:
            my_range[0] = min(start, my_range[0], end)
            my_range[1] = max(start, end, my_range[1])
        elif start <= my_range[0] <= my_range[1] <= end:
            my_range[0] = start
            my_range[1] = end
        #print(my_range)
        
    
    print(my_range[1] - my_range[0] + 1)

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()