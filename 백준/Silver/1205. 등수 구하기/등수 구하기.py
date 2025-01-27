import sys

input = sys.stdin.readline

N, newScore, P = map(int, input().split())

if N == 0:
    print(1)
else:
    inputList = list(map(int, input().split()))

    rank = 1  # 새로운 점수의 랭킹
    boundary = 1  # 점수 변하는 시점

    for i in range(N):
        # 순위 밀림
        if inputList[i] > newScore:
            rank += 1
            boundary += 1
        # 순위 유지
        elif inputList[i] == newScore:
            boundary += 1

    # 랭킹이 꽉 찼으면 -1을 출력
    if boundary > P:
        print(-1)
    else:
        print(rank)