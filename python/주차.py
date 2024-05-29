'''
n = 주차공간 수 입력 ( C:점유 , .:비어있음 )
어제 오늘 모두 주차공간 점유된 개수 구하기
'''

YT_info = 0

n = int(input('주차 공간 수 : '))

yesterday = input('어제 주차 정보 : ').upper()
if(len(yesterday) == n):
    today = input('오늘 주차 정보 : ').upper()
    if(len(today) == n):
        for i in range(0,n):
            if(yesterday[i] =='C' and today[i]=='C'):
                YT_info += 1
        print(f'어제 오늘 점유된 주차 공간 수는 {YT_info}입니다.')
    else:
        print('wrong yesterday info')
else:
    print('wrong yesterday info')