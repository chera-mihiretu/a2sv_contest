from sys import stdin,stdout
from bisect import *
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    Q, N = [int(i) for i in input().split()]
    array = []
    index = []
    ind = 0
    MOD = pow(10, 18)
    for _ in range(Q):
        command, number = [int(i) for i in input().split()]
        if MOD < ind:
            continue
        if command == 1:
            ind += 1
            array.append(number)
            index.append(ind)
        else:
            ind = (ind) * (number + 1)
            
        

    query = [int(i) for i in input().split()]
    answer = []
    for i in query:
        remain = i
        while True:
            cur_ind = bisect_left(index, remain)
            if cur_ind  < len(index) and remain % index[cur_ind] == 0:
                answer.append(array[cur_ind])
                break
            elif cur_ind - 1 > 0 and remain % index[cur_ind - 1] == 0:
                answer.append(array[cur_ind - 1])
                break
            else:
                remain = remain % index[cur_ind - 1]
    print(*answer)            
    






# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()
