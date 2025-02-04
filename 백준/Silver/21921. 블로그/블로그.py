import sys
input = sys.stdin.readline

# 슬라이딩 윈도우다!
N, X = map(int, input().split(' '))

visitCount = list(map(int, input().split(' ')))

index = 1
currentSum = sum(visitCount[:X])
maxSum = currentSum
count = 1

while index + X - 1 < N:
    currentSum = currentSum - visitCount[index-1] + visitCount[index+X-1]

    if currentSum > maxSum:
        maxSum = currentSum
        count = 1
    elif currentSum == maxSum:
        count += 1

    index += 1


if maxSum == 0:
    print("SAD")
else:
    print(maxSum)
    print(count)
