import sys
input = sys.stdin.readline

N = int(input())

# 빨리 끝나는 회의 순서대로 정렬해야 함!! ** 
# end_time을 체크두고, 반복문 탐색
# 시작 시간이 이전에 체크한 end_time보다 같거나 더 큰 경우 카운팅
# 끝나는 시간이 같다면 일찍 시작하는 애 먼저 카운팅 되어야 함
"""
ex)
2 2
1 2
순서로 되어있다면 2 2 먼저 선택될 경우 1 2는 무시됨
1 2 먼저 선택되면 2 2는 선택 가능 
=> 1. 끝나는 시간순 정렬 -> 2. 빨리 시작하는 시간순 정렬 
"""
timetable = [list(map(int, input().split())) for _ in range(N)]

timetable.sort(key = lambda x: (x[1], x[0]))
# print(timetable)

count = 1
end_time = timetable[0][1]
for i in range(1,N):
    if(end_time <= timetable[i][0]):
        # print(timetable[i])
        count += 1
        end_time = timetable[i][1]

print(count)