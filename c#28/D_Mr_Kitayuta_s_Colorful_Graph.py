from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    parent = [i for i in range(n + 1)]
    def find(x):
        if x != parent[x]:
            x = find(parent[x])
            return parent[x]
        return parent[x]
    def union(one, two):
        parent[find(one)] = find(two)
    color = []
    for _ in range(m):
        color.append([int(i) for i in input().split()])
    
    q = int(input())
    query = []
    for _ in range(q):
        query.append([int(i) for i in input().split()])



    color.sort(key=lambda x: x[-1])

    


    start = color[0][2]
    
    answer = [0 for i in range(q)]
    for i in range(m):
        if start == color[i][2]:
            union(color[i][0], color[i][1])
        else:
            
            for j in range(q):
                if find(query[j][0]) == find(query[j][1]):
                    answer[j] += 1
            for _ in range(n + 1):
                parent[_] = _
            start = color[i][2]
            union(color[i][0], color[i][1])
    for j in range(q):
        if find(query[j][0]) == find(query[j][1]):
            answer[j] += 1
    print(*answer, sep='\n')


    
   


    
    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()