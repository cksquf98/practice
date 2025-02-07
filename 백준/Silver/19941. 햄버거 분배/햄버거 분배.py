import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split(' '))  # 식탁의 길이 N, 햄버거 먹을 수 있는 거리 K

table = list(input().rstrip())
hamburgerLocation = deque([])
peopleLocation = deque([])

count = 0

for i in range(N):
    if table[i] == 'H':
        hamburgerLocation.append(i)
    else:
        peopleLocation.append(i)


while hamburgerLocation and peopleLocation:
    hamburgerIndex = hamburgerLocation.popleft()
    personIndex = peopleLocation.popleft()
    if abs(hamburgerIndex - personIndex) <= K:
        count += 1
    # 햄버거보다 사람이 오른쪽에 있는 경우 -> 사람은 오른쪽 햄버거를 먹을 수도 있음!! 사람을 다시 넣어
    elif hamburgerIndex < personIndex:
        peopleLocation.appendleft(personIndex)
    # 햄버거보다 사람이 왼쪽에 있는 경우 -> 나중에 올 사람이 얘를 먹을 수도 있음!! 햄버거 다시 넣어
    elif hamburgerIndex > personIndex:
        hamburgerLocation.appendleft(hamburgerIndex)


print(count)
