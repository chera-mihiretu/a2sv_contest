from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    lanes, desks, k = [int(i) for i in input().split()]
    table = 1
    for lane in range(1, lanes + 1):
        for desk in range(1, desks + 1):
            
            if table == k:
                return (lane , desk, 'L')
            elif table + 1 == k:
                return (lane , desk , 'R')
            table += 2
            
    

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        print(*solution())