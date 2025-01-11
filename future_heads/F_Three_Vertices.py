import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())

    graph = [[] for i in range(n)]

    for _ in range(n-1):
        fr, to = [int(i) for i in input().split()]

        graph[fr-1].append(to-1)
        graph[to-1].append(fr-1)
    
    node = max(range(n), key=lambda x : len(graph[x]))
    res = 0
    indexes = []
    def rec(node, parent):
        nonlocal res, indexes
        if len(graph[node]) == 1:
            return [[1, node]]
        answer = []
        for child in graph[node]:
            if child != parent:
                result = rec(child, node)
                answer.extend(result)
                answer.sort(reverse=True)
                answer = answer[:3]
        
        total = 0
        for i in answer: 
            total += i[0]

        if total > res:
            res = total
            indexes = [i[1]+1 for i in answer]
        answer = answer[:2]
        answer[0][0]  += 1
        return answer
    
    rec(node, -1)
    print(res)
    if len(indexes) != 3:
        for i in range(n):
            if (i + 1) not in indexes:
                indexes.append(i+1)
                break
    print(*indexes)

       
    



                


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()