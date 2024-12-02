from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    total = int((n*(1 + n)) / 2)
    

    twos = 1


    while twos <= n:
        total -= 2 * twos
        twos <<= 1

    print(int(total))

    
    
# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()


        