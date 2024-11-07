# n=int(input())
# char=input()+'w'
# l=0
# count=0
# group=0
# ans=[]
# flag=False
# for r in range(n):
#     if char[r]=="B":
#         count+=1
#     else:
#         if count>0:
#             group+=1
#             ans.append(count)
#             flag=True
#         count=0
#     if not flag:
#        ans.append(count)
# print(group)
# print(*ans)

from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n = int(input())
    string = input()

    answer = []
    count = 0
    for i in range(n):
        if string[i] == 'W':
            if count != 0:
                answer.append(count)
            count = 0
        else:
            count  += 1
    if count:
        answer.append(count)
    print(len(answer))
    print(*answer)
        


# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()