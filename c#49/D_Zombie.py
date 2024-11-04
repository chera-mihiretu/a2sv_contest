
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m = [int(i) for i in input().split()]
    graph = [ [] for i in range(n + 1)]

    answer = 0

    for _ in range(m):
        fr, to= [int(i) for i in input().split()]
        graph[to].append(fr)
        graph[fr].append(to)


    def calculcate(node, pre):
        nonlocal answer
        child_distance = 0


        for i in graph[node]:
            if i != pre:
                current = calculcate(i, node)
                answer = max(answer, current + child_distance)
                child_distance = max(child_distance, current)
        return child_distance + 1
    calculcate(1, -1)

    print(answer)

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
