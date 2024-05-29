'''
1. 모든 가맹점의 총 매출액이 13배수인 날 : 총 매출액 / 13 몫 >> 보너스
2. 모든 가맹점에 대해 하루 총 매출이 13배수 : 하루 매출 / 13 몫 >> 보너스

input : 가맹점의 수 f, 영업일수 d / 가맹점 당 하루 매출액(d줄 입력)
output : 총 보너스액

이중리스트 활용!!!하면 된대
'''

bonus = 0
table = []


F,D = map(int, input('가맹점의 수와 영업일수를 입력하시오. : ').split())

for i in range(D):
    # int 변환 필요.... 이거 에바지 바로 변환해주는 메소드가 없나..?;;
    data = input('매출 입력 :').split() # 리스트 형태로 저장됨
    for j in range(F):
        data[j] = int(data[j]) # 바꿔서 제자리 저장
    table.append(data)




# column 합 구하려면 sum()함수 사용하기 (한 가맹점의 총 매출)
for col in table:
    totalChain_day = sum(col)
    if(totalChain_day % 13 == 0):
        # print(totalChain_day)
        bonus += (totalChain_day // 13)


# 하루 당 총 가맹점의 매출액 합
for f in range(F):
    totalChain_day = 0
    for d in range(D):
        totalChain_day = totalChain_day + (table[d][f])
    if(totalChain_day % 13 == 0):
        bonus = bonus + (totalChain_day // 13)

print(bonus)