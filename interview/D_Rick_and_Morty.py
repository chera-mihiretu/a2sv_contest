from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    a,b = [int(i) for i in input().split()]
    c,d = [int(i) for i in input().split()]
    set_a = set()
    set_b = set()


    for i in range(1000):
        a_jump = b + (i * a)
        b_jump = d + (i * c)
        set_a.add(a_jump)
        set_b.add(b_jump)

        if a_jump in set_b :
            return a_jump
        elif b_jump in set_a:
            return b_jump
    return -1




        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        print(solution())