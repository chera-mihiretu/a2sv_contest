from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    m,n,w = [int(i) for i in input().split()]
    weight = [int(i) for i in input().split()]
    beauty = [int(i) for i in input().split()]
    parent = [i for i in range(n)]
    rank = [[be, we] for be, we in zip(beauty, weight)]
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
            return parent[x]
        return parent[x]
    def union(x, y):
        if find(x) != find(y):
            parent[x] = find(y)
            rank[x] = [rank[x][0] + rank[y][0], rank[x][1] + rank[y][1]]





    for _ in range(m):
        fr, to = [int(i) for i in input().split()]
        union(fr, to)
    

    def pickNotPick(index):

        if index == n:
            return [0,0]
        
        group = pickNotPick(index+1, )
        single = 


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()