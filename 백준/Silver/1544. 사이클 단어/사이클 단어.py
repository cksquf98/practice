import sys
from collections import deque
input = sys.stdin.readline

words = deque()
N = int(input())
for _ in range(N):
    new_str = input().rstrip()
    
    # 현재 문자열이 words에 이미 있는지 확인
    if new_str in words:
        continue

    is_circular = False
    for word in words:
        if len(word) == len(new_str):
            # 문자열이 같은 길이일 경우, 순환 문자열인지 확인
            if len(word) > 0 and (new_str in (word + word)):
                is_circular = True
                break
    
    if not is_circular:
        words.append(new_str)

print(len(words))
