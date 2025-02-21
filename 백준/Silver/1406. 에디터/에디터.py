import sys
from collections import deque
input = sys.stdin.readline

# L: move left, D: move right, B: delete left, P: add left
# 문자열의 최대 길이는 60만이므로 커서에 따라 리스트를 수정하는 방식은 시간 복잡도가 높아 시간 초과가 발생합니다.
# 그러므로 커서는 그대로 둔 채 커서 기준 좌측, 우측 리스트에 문자를 입력하는 방식으로 풀어야 합니다.

origin = input().rstrip()
commandNum = int(input())
leftString = deque([])
rightString = deque([])

for char in origin:
    leftString.append(char)

for _ in range(commandNum):
    command = input().rstrip().split(' ')

    if len(command) == 1:
        command = command[0]
    else:
        addStr = command[1]
        command = command[0]

    if command == "L" and len(leftString) > 0:
        rightString.appendleft(leftString.pop())
    elif command == "D" and len(rightString) > 0:
        leftString.append(rightString.popleft())
    elif command == "B" and len(leftString) > 0:
        leftString.pop()
    elif command == "P":
        leftString.append(addStr)
        
left = ''.join(leftString)
right = ''.join(rightString)
print(left + right)