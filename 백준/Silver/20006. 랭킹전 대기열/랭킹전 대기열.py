import sys
input = sys.stdin.readline

p, m = map(int, input().split(' '))  # 플레이어 수, 방 정원

totalRoomList = []

def findRoom(roomList, level, nickname):
    for room in roomList:
        if len(room) < m and abs(room[0][0] - level) <= 10:
            room.append((level, nickname))
            return roomList

    roomList.append([(level, nickname)])
    return roomList


for _ in range(p):
    level, nickname = map(str, input().rstrip().split(' '))
    level = int(level)
    totalRoomList = findRoom(totalRoomList, level, nickname)

for room in totalRoomList:
    if len(room) == m:
        print("Started!")
        for roomDetail in sorted(room, key=lambda x: x[1]):
            print(f"{roomDetail[0]} {roomDetail[1]}")
    else:
        print("Waiting!")
        for roomDetail in sorted(room, key=lambda x: x[1]):
            print(f"{roomDetail[0]} {roomDetail[1]}")