import sys

N, M = map(int, sys.stdin.readline().split())

#N개 정수 입력
n_list = [*map(int, sys.stdin.readline().split())]

total = 0


#그냥 count에 저장하면 시간초과 남 => 구간 합 저장하는 리스트를 미리 만들기
sum = []
for l in range(0,N):
    total += n_list[l]
    # print(total)
    sum.append(total)


for i in range(0,M):
    start, end = map(int, sys.stdin.readline().split())
    if(start-1 > 0):
        print(sum[end-1] - sum[start-2])
    else:
        print(sum[end-1])