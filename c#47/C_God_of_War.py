from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    no_caves = int(input())
    caves = []
    for _ in range(no_caves):
        caves.append([int(i) for i in input().split()])

    start_end = []

    for i in range(no_caves):
        start = caves[i][1] + 1
        for j in caves[i][1:]:
            if j < start:
                start += 1
            else:
                start = start + (j - start) + 2
        
        start_end.append([start - len(caves[i][1:]),start])
    # print(start_end)
    start_end.sort()
    start = start_end[0][0]
    end = start_end[0][1]
    for i in range(1, len(start_end)):
        if end < start_end[i][0]:
            start += start_end[i][0] - end
            end += start_end[i][0] - end
        end += start_end[i][1] - start_end[i][0]
   
    print(start)


    

# run the code
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        solution()