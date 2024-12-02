from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    h_s, m_s = [int(i) for i in input().split(':')]
    h_t, m_t = [int(i) for i in input().split(':')]

    h = (h_s - h_t) % 24


    m = (m_s - m_t) % 60

    h += 1 if ((m_s - m_t) >=  60) else 0 
    


    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)

    print(str(h) + ':' + str(m))


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()