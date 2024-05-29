'''

두줄의 input : 1 < r,h < 100
원뿔의 부피 : PI * 반지름^2 * 높이

'''

flag = True
while (flag):
    r = int(input('반지름 : '))
    h = int(input('높이 : '))
    if ((r>1 and r<100) and (h>1 and h<100)):
        flag = False
    else:
        print('입력값은 1부터 100사이 숫자입니다.')


PI =  3.141592
V = (PI * r**2 * h)/3
print(f'원뿔의 부피는 {V}입니다아아')