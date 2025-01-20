# 공동 2등 다음은 4등부터 시작된다는 조건이 있닷

import sys
input = sys.stdin.readline

# 국가의 수 N, 등수 출력할 국가 K
N, K = map(int, input().rstrip().split(' '))


# 각 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수 입력
countries = [list(map(int, input().split(' '))) for _ in range(N)]

countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True) #x[0]은 국가 번호

# 등수만 쫙 정리?!
rank = {}
ranking = 1 # 등수 체크
count = 0 # 공동 등수 체크용 count

current = countries[0][1:]

for i in range(N):
    country = countries[i][0]
    medal = countries[i][1:]
    if(current != medal):
        ranking += count
        current = medal
        count = 1
    else:
        count += 1
    # print(count)
    rank[country] = ranking

print(rank[K])