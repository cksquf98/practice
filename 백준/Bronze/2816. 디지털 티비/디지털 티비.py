import string
import sys
input = sys.stdin.readline

# 방법이 최소일 필요는 없나본디???
# 그럼 그냥 무조건 먼저 KBS채널을 찾고 위로 끌고오는 방법으로 해야겟디 하하

N = int(input())
channels = [input().rstrip() for _ in range(N)]
controller = ''

i = 0

while not (channels[0] == 'KBS1' and channels[1] == 'KBS2'):
    if (channels[i] == 'KBS1' and i != 0):
        controller += '4' * i
        channels.pop(i)
        channels.insert(0, 'KBS1')
        i = 0

    elif (channels[i] == 'KBS2' and i != 1):
        controller += '4' * (i - 1)
        channels.pop(i)
        channels.insert(1, 'KBS2')
        i = 1

    else:
        controller += '1'
        i += 1

print(controller)