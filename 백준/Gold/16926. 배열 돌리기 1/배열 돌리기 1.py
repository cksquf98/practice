"""
5 6 3
1 18 17 16 15 14
2 1 10 9 8 13
3 2 1 2 7 12
4 3 4 5 6 11
5 6 7 8 9 10

길이가 1인 inner 사각형은 회전 안된다는 점... <- 이건 이해 안감
"""

# 겉 테두리가 하나의 deque임
# r번 회전 시 -> 맨 뒤 r개의 원소를 맨 앞으로 넣어주면 됨 = deque.rotate(r) 사용
# 출력이 좀 까다로울 듯

# for문 역순 출력 : for( 시작위치, 종료위치-1, -1 )

import sys
input = sys.stdin.readline

N, M, r = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]


#덱 생성
from collections import deque



#테두리 개수
inner_cnt = min(N,M) // 2

for i in range(inner_cnt):
    deq = deque()

    #덱에 좌측 테두리 넣기
    for left in range(i,N-i):
        deq.append(arr[left][i])

    #덱에 하단 테두리 (양 끝 빼고) 넣기
    for bottom in range(i+1, M-i-1):
        # print("bottom -> ",bottom)
        deq.append(arr[N-i-1][bottom])

    #덱에 우측 테두리 넣기
    for right in range(N-i-1, i-1, -1):
        # print("right -> ",right)
        deq.append(arr[right][M-i-1])

    #덱에 상단 테두리 (양 끝 빼고) 넣기
    for top in range(M-i-2, i, -1):
        # print("top -> ",top)
        deq.append(arr[i][top])

    # 테두리 반시계 회전
    deq.rotate(r)

    # arr 맞는 위치에 저장하기
    #좌측 테두리
    for left in range(i,N-i):
        arr[left][i] = deq.popleft()

    #하단 테두리 (양 끝 빼고)
    for bottom in range(i+1, M-i-1):
        arr[N-i-1][bottom] = deq.popleft()

    #우측 테두리
    for right in range(N-i-1, i-1, -1):
        arr[right][M-i-1] = deq.popleft()

    #상단 테두리 (양 끝 빼고)
    for top in range(M-i-2, i, -1):
        arr[i][top] = deq.popleft()


for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()