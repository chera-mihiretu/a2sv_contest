# Blank

from sys import stdin,stdout
from functools import cmp_to_key
# take input
input = lambda: stdin.readline().strip()

def compareEach(string1, string2):
    pref = min(len(string1), len(string2))
    if string1[:pref] == string2[:pref]:
        if string1  + string2 >= string2 + string1:
            return True
        else:
            return False
    else:
        if string1 > string2:
            return True
        return False



def merge(left, right):
    left_ptr = 0
    right_ptr = 0
    answer = []
    while right_ptr < len(right) and left_ptr < len(left):
        if not compareEach(left[left_ptr], right[right_ptr]):
            answer.append(left[left_ptr])
            left_ptr += 1
        else:
            answer.append(right[right_ptr])
            right_ptr += 1
    
    answer.extend(right[right_ptr:])
    answer.extend(left[left_ptr:])
    
    return answer

def mergeSort(string, start, end):
    if end == start:
        return [string[start]]
    mid = start + (end - start) // 2

    left = mergeSort(string, start, mid)
    right = mergeSort(string, mid + 1, end)

    return merge(left, right)






    
    

# solution


def solution():
    
    n = int(input())

    strings = []
    for i in range(n):
        strings.append(input())

    answer = mergeSort(strings,0 ,len(strings) - 1)
    
    print(''.join(answer))

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()