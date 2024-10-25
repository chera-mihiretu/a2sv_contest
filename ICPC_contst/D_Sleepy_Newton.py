# blank ( 2 sami, chera)
from collections import defaultdict
from sys import stdin,stdout
# take input
input = lambda: stdin.readline().strip()
# solution
def solution():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    t = [int(i) for i in input().split()]

    left = 0
    l, r = 0, 0
    
    z = 0
    z_mx = 0

    cnt = 0
    mx = 0
    for right in range(n):
        cnt += a[right]
        if t[right] == 0:
            z += 1
        
        while right - left + 1 > k:
            cnt -= a[left]
            if t[left] == 0:
                z -= 1
            left += 1
        
        if z:
            if cnt > mx:
                l= left
                r = right
                mx = cnt
                z_mx = z
            elif cnt == mx:
                if z > z_mx:
                    l= left
                    r = right
                    z_mx = z
        
    ans = 0
    for i in range(n):
        if l <= i <= r:
            ans += a[i]
        else:
            ans += (a[i] * t[i])

    print(ans)




# run the code
if __name__ == '__main__':
    test_case = 1 #int(input())
    for i in range(test_case):
        solution()