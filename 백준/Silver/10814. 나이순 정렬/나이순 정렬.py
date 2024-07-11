#병합정렬로 풀까 생각해봤는데 ㅋㅎ 내장함수 써야지
import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    num, str = input().rstrip().split()
    arr.append([int(num), str])

arr = sorted(arr, key=lambda x: (x[0]))

for elem in arr:
    print(elem[0], elem[1], end=' ')
    print()