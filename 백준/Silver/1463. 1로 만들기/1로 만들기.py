import sys
from math import sqrt

input = sys.stdin.readline

num = int(input())

#시간제한 빡셈 -> 동적 계획법 사용 필요
#num까지 숫자들의 연산 횟수를 담아두는 배열 dp
dp = [0 for _ in range(num+1)]
dp[1] = 0

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1     #일단 -1연산 적용한걸로 저장해두고

    if(i % 3 == 0):
        dp[i] = min(dp[i], dp[i//3] + 1)    #나누기 연산 가능한지에 따라 횟수 비교
    
    if(i % 2 == 0):
        dp[i] = min(dp[i], dp[i//2] + 1)


print(dp[num])