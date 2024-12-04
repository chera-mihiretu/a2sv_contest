import sys, threading
input = lambda: sys.stdin.readline().strip()


class SegmentedTree:
    def __init__(self, array):
        self.n = len(array)
        self.arr = array
        self.tree  = [0] * (4 * self.n)
    def getChild(self, node):
        return [2 * node + 1, 2 * node + 2]
    

    def build(self, node, left, right):
        if left == right:
            self.tree[node] = self.arr[left]
            return 
        
        left_child, right_child = self.getChild(node)

        mid = left + (right - left) // 2

        self.build(left_child, left, mid)
        self.build(right_child, mid + 1, right)
    def update(self, node, left, right, u_left, u_right):
        if u_left > u_right:
            return
        if left == u_left and right == u_right:
            self.tree[node] = []
            return
        left_child, right_child = self.getChild(node)
        mid = left + (right - left) // 2
        self.tree[node] = 0
        if mid >= u_right:
            self.tree[right_child] = []
        if mid < u_left:
            self.tree[left_child] = []

        self.update(left_child, left, mid, u_left, min(mid, u_right))
        self.update(right_child, mid + 1, right, max(mid + 1, u_left), u_right)
        
    def query(self, node, left, right, index):
        if left == right:
            if self.tree[node] is  None:
                return ['b', ]










def main():
    n, m = [int(i) for i in input().split()]

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    segment = SegmentedTree(a)
    answer = []
    for _ in range(m):
        # these is where things go
        pass

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
