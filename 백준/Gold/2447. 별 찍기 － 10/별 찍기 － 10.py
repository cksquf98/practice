    # 9: 한 덩어리는 3의 패턴으로 이루어져 있음
    # 27: 한 덩어리는 9의 패턴으로 이루어져 있음


def makingStar(num):
    if(num == 1): 
        return ['*']
    
    stars = makingStar(num // 3) #N//3패턴
    
    result = []  #함수가 1번 돌 때의 결과를 담아둘 리스트

    #Top Line
    for star in stars:
        result.append(star*3)

    #Middle Line
    for star in stars:
        result.append(star + ' '*(num//3) + star)

    #Bottom Line 
    for star in stars:
        result.append(star*3)

    return result




import sys
N = int(sys.stdin.readline())
print('\n'.join(makingStar(N)))