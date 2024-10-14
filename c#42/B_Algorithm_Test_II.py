from sys import stdin,stdout
from collections import deque
# take input
input = lambda: stdin.readline().strip()
# solution
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self) -> str:
        def get(root):
            if root.val == None:
                return {'None'}
            my_val = {'head' : root.val, 'next' : get(root.next)}
            return my_val
        return str(get(self))

def solution():
    dummy = ListNode(None)
    tail = ListNode(None, prev=dummy)
    dummy.next = tail
    command_number = int(input())
    all_heads = {}
    for _ in range(command_number):
        command_name, *numbers  = input().split()
        if command_name == 'insert':
            insert, after = [int(i) for i in numbers]
            if after in all_heads:
                to_be_insertd = all_heads[after][0]
                hold = to_be_insertd.next
                to_be_insertd.next = ListNode(insert, hold, to_be_insertd)
                all_heads[insert].append(to_be_insertd.next)
            else:
                tail.prev.next = ListNode(insert, tail, tail.prev)
        else:
            if int(numbers[0]) in all_heads:
                to_be_removed = all_heads[numbers[0]][0]
                to_be_removed.prev.next = to_be_removed.next
                all_heads[numbers[0]].popleft()
    print(all_heads)
    current = dummy.next
    answer= []
    while current.val != None:
        answer.append(current.val)
    print(*answer)





# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()