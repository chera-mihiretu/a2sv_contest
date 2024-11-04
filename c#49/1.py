from sys import stdin 
from collections import Counter
input  = lambda : stdin.readline().strip()

def solution():
    string = input()

    count = Counter(string)
    red = 0
    green = 0
    for item, freq in count.items():
        if freq == 1:
            if red < green:
                red += 1
            else:
                green += 1
        else:
            green += 1
            red += 1
    print(min(red, green))


if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        solution()
