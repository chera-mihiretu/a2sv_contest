from sys import stdin 
#from collections import defaultdict


def solution():
    length = int(input())
    nums = [int(i) for i in input().split()]
    
    negatives = []
    posatives = []
    zeros = []
    for num in nums:
        if num > 0:
            posatives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zeros.append(num)

    if not posatives:
        posatives.append(negatives.pop())
        posatives.append(negatives.pop())

    if (len(negatives) % 2) == 0:
        zeros.append(negatives.pop())

    #print(negatives, posatives, zeros)
    print(len(negatives), *negatives)
    print(len(posatives), *posatives)
    print(len(zeros), *zeros)



if __name__ == '__main__':
    solution()
