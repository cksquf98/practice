import sys
input = sys.stdin.readline

"""
개총 시작시각 S <<얘 시작 전에 입장 여부 확인 :시작 시간 이전 채팅 기록으로
종료시각 E ~ 스트리밍 끝 시각 Q << 퇴장 여부 확인 : 사이에 채팅 기록으로

입퇴장 모두 확인되는 인원 수 구하기
"""

S,E,Q = input().rstrip().split()

start_hour, start_minute = map(int, S.split(":"))
end_hour, end_minute = map(int, E.split(":"))
streaming_end_hour, streamning_end_minute = map(int, Q.split(":"))

attendance = {}

for line in sys.stdin:
    time, name = line.rstrip().split()
    hour, minute = map(int, time.split(":"))


    # print("시작시간 비교: ", hour, start_hour, minute, start_minute)
    if(hour == start_hour):
       if(minute <= start_minute):
        attendance[name] = 0 #출석부에 일단 이름은 추가
    elif(hour < start_hour):
        attendance[name] = 0

    # print("종료시간 비교 : ", hour, end_hour, minute, streaming_end_hour, streamning_end_minute)
    # 완전 if문으로 다다닥 비교하지 않고 변수로 아예 조건 만들어서 얘네를 비교해서 걸러보자ㅏㅏ
    after_end_time = (hour > end_hour) or (hour == end_hour and minute >= end_minute)
    before_streaming_end = (hour < streaming_end_hour) or (hour == streaming_end_hour and minute <= streamning_end_minute)

    if after_end_time and before_streaming_end:
        if(attendance.get(name)!= None):
            attendance[name] = 1
cnt = 0
for v in attendance.values():
    if(v == 1):
        cnt+=1
print(cnt)