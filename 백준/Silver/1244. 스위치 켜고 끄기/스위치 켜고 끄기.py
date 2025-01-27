import sys
input = sys.stdin.readline

switchNum = int(input())
switch = [-1]
switch.extend(list(map(int, input().split(' '))))

studentNum = int(input())


def changeSwitchNum(index):
    if 1 <= index <= switchNum:
        if switch[index] == 0:
            switch[index] = 1
        else:
            switch[index] = 0


def toggle(gender, index):
    # 남학생 == 1 : 받은 수의 배수 스위치를 toggle
    if gender == 1:
        for i in range(index, switchNum+1, index):
            changeSwitchNum(i)

    # 여학생 == 2 : 인덱스 + j / 인덱스 - j을 대칭일때까지 비교해서 싹 toggle
    else:
        j = 1
        changeSwitchNum(index)
        while index - j >= 1 and index + j <= switchNum:
            if switch[index-j] == switch[index+j]:
                changeSwitchNum(index-j)
                changeSwitchNum(index+j)
                j += 1

            else:
                break
            # print(switch)


for i in range(studentNum):
    gender, index = map(int, input().split(' '))
    toggle(gender, index)

# 아놔,, 출력 뭐야 이거
for i in range(1, switchNum + 1):

    print(switch[i], end=' ')

    # 20개 줄바꿈
    if i % 20 == 0:
        print()
