'''
한달 데이터양 : X (1~100)
데이터 사용 개월 수 : N (1~100)
N개월 별 데이터 사용량 입력 (0 ~사용 가능 데이터량 이하)

출력 : 다음달 사용 가능한 데이터양
'''
flag1 = True
flag2 = True
while(flag1 and flag2):
    month_data = int(input('한 달 데이터양 : '))
    if(1 <= month_data <= 100 ):
        flag1 = False

    month = int(input('데이터 사용 개월 수 : '))
    if(1 <= month <= 100):
        flag2 = False

total = month_data * (month + 1) # 다음 달까지 받는 총 데이터 합산량

for i in range(0,month):
    used = int(input('이번 달 사용량 : '))
    if (used >= total):
        total -= month_data
    else:
        total-=used

print(f'다음 달 사용 가능 데이터 : {total}')