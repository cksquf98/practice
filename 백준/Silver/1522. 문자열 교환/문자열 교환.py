import sys
from collections import deque
input = sys.stdin.readline

circle_string = list(input().rstrip())

b_count = circle_string.count('b')

circle_string.extend(circle_string[:b_count])

slide = deque(circle_string[:b_count])
current = slide.count('b')
max_count = current

if b_count > 0:
    for i in range(b_count, len(circle_string)):
        left = slide.popleft()
        if left == 'b':
            current -= 1

        if circle_string[i] == 'b':
            current += 1
        slide.append(circle_string[i])

        max_count = max(current, max_count)

print(b_count - max_count)
