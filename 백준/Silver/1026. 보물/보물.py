import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

A_re = sorted(A)
B_re = sorted(B, reverse=True)

ans = 0
for i in range(N):
    ans += A_re[i] * B_re[i]

print(ans)