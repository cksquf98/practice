import sys
from collections import deque
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(elem for elem in map(int, input().split()))
#덱을 써서 흠... 합산하고 앞에 애 pop -> 다음 애 push
slide = deque()
max_visit = 0
count = 1
for i in range(X):
    max_visit += visit[i]
    slide.append(visit[i])

# print("start : ", max_visit)

current = max_visit
for j in range(1, N-X+1):
    current -= slide.popleft()
    current += visit[j+X-1]
    slide.append(visit[j+X-1])

    # print("slide : ",slide)
    # print(current)

    if(current > max_visit):
        max_visit = current
        count = 1
    elif(current == max_visit):
        count += 1


if(max_visit == 0):
    print("SAD")
else:
    print(max_visit)
    print(count)