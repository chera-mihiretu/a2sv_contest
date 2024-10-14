from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b,c,d = [int(i) for i in input().split()]

    paul = max((3*a)/10, a - (a / 250) * c)
    mighty = max((3*b)/10, b - (b / 250) * d)

    if paul > mighty:
        print("Misha")
    elif paul < mighty:
        print("Vasya")
    else:
        print("Tie")

# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()