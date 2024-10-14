
from sys import stdin
from collections import Counter


input = lambda : stdin.readline().strip()

def solution():
    n = int(input())
    hash_map = Counter()
    total = []
    for _ in range(n):
        line = input().split()
        if line[0] == '1':
            from_node, to_node, cost = [int(i) for i in line[1:]]
            
            while from_node != to_node:
                if from_node < to_node:
                    change_to = to_node // 2
                    hash_map[(change_to, to_node)] += cost
                    to_node = change_to
                else:
                    change_to = from_node // 2
                    hash_map[(change_to, from_node)] += cost
                    from_node = change_to  
        else:   
            answer = 0
            from_node, to_node = [int(i) for i in line[1:]]
            while from_node != to_node:
                if from_node < to_node:
                    change_to = to_node // 2
                    answer += hash_map[(change_to, to_node)]
                    to_node = change_to
                else:
                    change_to = from_node // 2
                    answer += hash_map[(change_to, from_node)]
                    from_node = change_to
            total.append(answer)
    print(*total, sep='\n')


if __name__ == '__main__':
    solution()
