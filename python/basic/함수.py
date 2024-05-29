def coffee(shot=2, takeout=True, size='M'):
    print(f'{shot}/{size}')
    if takeout:
        print('포장 완료')
    else:
        print('inside')

coffee('S',takeout=False)


# 함수 전달값에서 가변인자 설정 : *변수  => 넘치는 파라미터는 다 요기로 처리됨
def ingredients(beans, water, *theOthers):
    out = ''
    a=[beans, water]
    for i in theOthers:
        a.append(i)

    for i in range(len(a)):
        if(i == len(a)-1):
            out += f'{a[i]}입니다.'
        elif(i == 0):
            out += f'재료는 {a[0]}, '
        else:
            out += f'{a[i]}, '
    return out
print(ingredients('커피콩','물 2리터', '우유스팀', '설탕', '핫초코'))

# 나는 "재료는 커피콩, 물 2리터, 우유스팀, 설탕입니다" 이렇게 출력하고픈데 이건 어케 하지?;; >> 해결 ㅎㅎㅎ


# 단어 수 세기 함수 : count()함수는 공백 카운트 함
def word_count(word):
    count = word.count(' ')+1
    return  count  
print(word_count('i wanna go back.. haha'))


# 리스트 값 삭제 함수
def remove_v(l,value):
    while value in l:
        l.remove(value)

    return l

l = [1,2,3,4,5,4,5]
print(remove_v(l,5))
print(l)

a= remove_v([3,4,1,2,3,4],3)
print(a)