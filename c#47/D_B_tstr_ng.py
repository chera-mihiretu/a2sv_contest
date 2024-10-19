from sys import stdin,stdout
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]
    string = list(input())
    start = 0
    for i in range(k, n ):
        if string[i] != string[start]:
            if string[i] == '?':
                string[i] = string[start]
            elif string[start] == '?':
                string[start] = string[i]
            else:
                print('NO')
                return
        start += 1
    count = Counter()
    for i in range(k):
        if string[i] == '?':
            count['1'] += 1
            count['0'] += 1
        else:
            count[string[i]] += 1
    
    if count['1'] < k//2 or count['0'] < k//2:
        print('NO')
        return
    start = 0
    for i in range(k, n):
        if string[i] == '?':
            count['1'] += 1
            count['0'] += 1
        else:
            count[string[i]] += 1

        if string[start] == '?':
            count['1'] -= 1
            count['0'] -= 1
        else:
            count[string[i]] -= 1
        if count['1'] < k//2 or count['0'] < k//2:
            print('NO')
            return
    print('YES')
        



            








    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()