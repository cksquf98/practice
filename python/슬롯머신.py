'''
N = 카지노 칩 개수

슬롯머신 A : 35번째 플레이한 유저에게 상금 칩30개
슬롯머신 B : 100번째 플레이한 유저에게 상금 60개
슬롯머신 C : 10번째 플레이한 유저에게 상금 9개

a > b > c 순서대로 돌아가면서 플레이
출력 : 남은 칩이 없을 때까지 플레이한 횟수
'''

n = int(input('칩 개수 : '))
slot_A = int(input('첫번째 슬롯 횟수 : '))
slot_B = int(input('두번째 슬롯 횟수 : '))
slot_C = int(input('세번째 슬롯 횟수 : '))
current_slot = 1  # 현재 플레이중인 슬롯 1 : A, 2 : B, 3 : C 사이클


#여기서 current_slot 없이 짜려면???    사이클 도는 연산은 %연산자 이용하기

plays = 0
while(n>0):
    if(plays%3  == 1):     # current_slot == 1
        slot_A += 1 
        n -= 1
        if(slot_A == 35):
            n += 30
            slot_A = 0
    elif(plays%3 == 2):     # current_slot == 2
        slot_B += 1
        n -= 1
        if(slot_B == 100):
            n += 60
            slot_B = 0
    else:
        slot_C += 1
        n-=1
        current_slot = 0  # 다시 첫번째 슬롯으로 보내려고 리셋
        if(slot_C == 10):
            n += 9
            slot_C = 0
    current_slot += 1
    plays += 1
print('plays : ',  plays)