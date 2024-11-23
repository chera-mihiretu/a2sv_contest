from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution is segented tree
class SegmentedTree:
    def __init__(self, n, array):
        self.ac_array = array
        self.array = [0] * (n * 4)
        self.fill(0, n - 1, 0)

    def fill(self, array_l, array_r, segment):
        if array_l == array_r:
            self.array[segment] = self.ac_array[array_l]
            return 
        left_child, right_child = self.getMeChildren(segment)
        mid = array_l + (array_r - array_l) // 2
        self.fill(array_l, mid, left_child)
        self.fill(mid + 1, array_r, right_child)

    def getMeChildren(self, root):
        return [root * 2 + 1, root * 2 + 2]
    
# solution
def solution():
    n,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    s = SegmentedTree(n, b)
    print(s.array)
    
    for _ in range(m):
        t, *command = [int(i) for i in input().split()]
        if t == 1:
            x, y, k = command
        else:
            index = command[0] 

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()