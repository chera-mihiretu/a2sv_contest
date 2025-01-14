from typing import *
from heapq import * 
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        root = self
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        return result
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        heap = []

        def dfs(root, target, k):
            if not root:
                return 
            heappush(heap, [-abs(root.val - target), root.val])

            if len(heap) > k:
                heappop(heap)

            dfs(root.left, target, k)
            dfs(root.right, target, k)
        dfs(root, target, k)
        answer = []
        
        for dis, val in heap:
            answer.append(val)
            
        return answer
            




def create_tree_from_array(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        # Create left child if value is not None
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Create right child if value is not None
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root



root = create_tree_from_array(eval(input()))
target =  float(input())
k = int(input())


s = Solution()
print(s.closestKValues(root, target, k))