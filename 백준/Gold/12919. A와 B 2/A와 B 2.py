import sys
from collections import deque
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# S->T가 가능하면 1, 불가능하면 0
# 근데 무조건 그럼 B로 시작해야 가능하지 않나???
# 모든 경우의 수를 따지니까 메모리 초과가 남
# 블로그 보니까 S->T로 만드는건 모든 수를 따져야하는데 T->S를 만드는건 한정되어있다는 힌트를 얻음
queue = deque([T])

res = False

while queue:
    candidate = queue.popleft()

    if candidate == S:
        res = True

    if len(candidate) < len(S):
        break

    elif len(candidate) == len(S):
        continue

    # 맨 앞 확인
    if candidate[0] == 'B':
        copy = candidate[::-1]
        copy = copy[:-1]
        queue.append(copy)

    # 맨 뒤 확인
    if candidate[-1] == 'A':
        queue.append(candidate[:-1])

print(int(res))