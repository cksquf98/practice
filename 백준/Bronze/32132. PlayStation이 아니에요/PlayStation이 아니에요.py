import sys
input = sys.stdin.readline


strLen = int(input().strip())
s = input().rstrip()

# 반복하여 숫자를 제거
while "PS4" in s or "PS5" in s:
    s = s.replace("PS4", "PS").replace("PS5", "PS")

print(s)