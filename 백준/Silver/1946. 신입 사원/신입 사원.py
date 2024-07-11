import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    res = 0

    arr = []
    for i in range(N):
        num1, num2 = map(int, input().split())
        arr.append([num1,num2])

    arr = sorted(arr, key = lambda x : x[0])    

    standard = arr[0][1]
    res += 1

    for idx in range(1,N):
        compare = arr[idx]
        if(compare[1] < standard):
            standard = compare[1]
            res += 1

    print(res)