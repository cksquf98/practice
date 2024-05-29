'''
재생목록 : ABCDE
버튼 1: 맨 앞 문자를 맨 뒤로 이동
버튼 2: 마지막 문자를 첫번째로
버튼 3: 첫번째 두번째 문자 스와핑
버튼 4: 재생 종료 

출력 : 공백으로 구분된 재생목록 순서
'''

list = 'ABCDE'
while(1):
    buttonNum = input('버튼 번호 : ')
    plays = int(input('횟수 : '))
    if(buttonNum == '4'):
        break
    else:
        if(buttonNum == '3'):
            for i in range(plays):
                list = list[1]+list[0]+list[2:]
        elif(buttonNum == '2'):
            for i in range(plays):
                list = list[-1]+list[:-1]
        elif(buttonNum == '1'):
             for i in range(plays):
                  list = list[1:]+list[0]

output=''
for i in list:
    output += i+' '
print(output)