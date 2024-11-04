
from sys import stdin 


input = lambda : stdin.readline().strip()
 
def solution():
    numbers = [4,6,9]

    array = [-float('inf') for i in range(16)]
    array[0] = 0
    for i in range(16):
        for j in {4, 6, 9}:
            if i - j >= 0:
                array[i] = max(array[i], array[i-j] + 1)
    q = int(input())

    for i in range(16):
        array[i] = max(-1, array[i])

    while q:

        n = int(input())

        if (n < 16):
            print(array[n])
        else:
            t = int((n - 16) / 4 + 1)

            print(t + array[n - 4 * t])
        
        q -= 1
if __name__ == '__main__':
    solution()
