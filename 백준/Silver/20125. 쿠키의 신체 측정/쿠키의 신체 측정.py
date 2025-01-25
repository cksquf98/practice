import sys
input = sys.stdin.readline

N = int(input())
cookie = list(input().rstrip() for _ in range(N))

head_c = -1
heart = [-1, -1]
armLength = [0, 0]
legLength = [0, 0]
waistLength = 0
leftLeg_c = -1
rightLeg_c = -1

for i in range(N):
    if head_c == -1 and '*' in cookie[i]:
        head_c = cookie[i].index('*')
        heart[1] = head_c

    elif '***' in cookie[i]:
        heart[0] = i
        for col in range(head_c):
            if (cookie[i][col] == '*'):
                armLength[0] += 1  # 왼쪽 팔 길이
        for col in range(head_c+1, N):
            if (cookie[i][col] == '*'):
                armLength[1] += 1  # 오른쪽 팔 길이

    # 허리가 아닌 경우 => 다리가 나오는 케이스 아닐까?!?!
    elif head_c != -1 and cookie[i][head_c] != '*':
        if waistLength == 0 and '*_*' in cookie[i]:
            waistLength = i - heart[0] - 1  # 다리 행 위치 - 심장 행 위치 - 1
            leftLeg_c = cookie[i].index('*')
            rightLeg_c = cookie[i].rindex('*')


        if rightLeg_c != leftLeg_c:
            if cookie[i][leftLeg_c] == '*':
                legLength[0] += 1
            if cookie[i][rightLeg_c] == '*':
                legLength[1] += 1
        elif leftLeg_c != -1 and rightLeg_c == leftLeg_c:
            if leftLeg_c > head_c:
                legLength[1] += 1
            elif leftLeg_c < head_c:
                legLength[0] += 1


print(f"{heart[0]+1} {heart[1]+1}")
print(
    f"{armLength[0]} {armLength[1]} {waistLength} {legLength[0]} {legLength[1]}")
