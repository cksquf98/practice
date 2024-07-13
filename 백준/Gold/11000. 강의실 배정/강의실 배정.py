import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
timetable = (list(map(int, input().split())) for _ in range(N))


#수업 시작 시간에 따라 정렬시켜서 끝나는 시간을 따로 체크해야 함 ***
timetable = deque(sorted(timetable,key=lambda x:(x[0], x[1])))
# end_time = [] #강의실 별 끝나는 시간을 체크하는 리스트 << for문으로 돌면서 찾으니까 메모리초과남


time = deque.popleft(timetable)[1]
end_time = [time] #for 메모리 초과 해결 => heapq
# end_time.append(time)


while(timetable):   
    time = timetable.popleft()

    # for i in range(len(end_time)):
    #     if(time[0] >= end_time[i]): #들어갈 수 있으면 기존 강의장에 넣고
    #         end_time[i] = time[0]
    #     else: #못들어가면 강의장 추가
    #         end_time.append(time[0])

    if(time[0] >= end_time[0]): #이 때 end_time[0] = 젤 빨리 끝나는 강의장
        #강의장 끝나는 시간 갱신 필요
        heapq.heappop(end_time)
        heapq.heappush(end_time, time[1])
    else:
        #새로운 강의장 추가
        heapq.heappush(end_time, time[1])

print(len(end_time))