from sys import stdin
from collections import Counter
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    pokemons = int(input())
    types = list(input())
    count = Counter()
    contains = set(types)
    pre = 0
    answer = float('inf')
    for i in range(pokemons):
        count[types[i]] += 1 
        while count[types[pre]] > 1:
            count[types[pre]] -= 1
            pre += 1
        if len(count) == len(contains):
            answer = min(answer, i - pre + 1)
    print(answer)


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()