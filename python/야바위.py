'''
A : 왼쪽 컵 - 가운데 컵 변경
B :  가운데 컵 - 오른쪽 컵 변경
C : 왼쪽 컵 - 오른쪽 컵 변경

공 위치는 왼쪽 컵에 있는 채로 시작
'''

ball_location = 1
switch = input('변경 방법 입력 : ').upper()
if(len(switch)>50):
    print("50자 이상 입력 불가")
else:
    for way in switch :
        if( way == 'A' and ball_location == 1 ):
            ball_location = 2
        elif (way == 'A' and ball_location == 2 ):
            ball_location = 1
        elif(way == 'B' and ball_location == 2):
            ball_location = 3
        elif(way == 'B' and ball_location == 3):
            ball_location = 2
        elif(way == 'C' and ball_location == 1):
            ball_location = 3
        elif(way == 'C' and ball_location == 3):
            ball_location = 1

print(ball_location)        