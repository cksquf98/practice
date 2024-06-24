import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
pair = {}
for i in range(N):
    pair[i] = time[i]


pair = dict(sorted(pair.items(), key = lambda x: x[1]))

total = 0
waiting_time = 0
for time in pair.values():
    total += (waiting_time+time)
    waiting_time += time
print(total)