'''
2인 플레이
높은 카드 : J K Q A
J : 뒤에 카드 1장 비교 > 1점
Q : 뒤에 카드 2장 비교 > 2점
K : 뒤에 카드 3장 비교 > 3점
A : 뒤에 카드 4장 비교 > 4점
뒤에 높은 카드 있으면 득점X

input : 카드 deck 순서
output : 득점 시 score 출력
'''

def cardCheck(cardDeck):
    '''
    cardDeck으로 온 리스트에 높은 카드가 있으면 False 반환
    '''
    if( 'J' or 'Q' or 'K' or 'A' in cardDeck):
        return False
    return True

cardDeck = []
cardNum = 52

for i in range(10):
    cardDeck.append(input('카드 입력: '))

playerA_score = 0
playerB_score = 0
playTurn = 'A Player'

for i in range(cardNum):
    getPoint = 0
    remaining = cardNum - i -1      # 남은 카드 개수 체크하는 변수
    card = cardDeck[i]
    if(card == 'J' and remaining >= 1 and cardCheck(cardDeck[i+1])):
        getPoint += 1
    elif(card == 'Q' and remaining >=2 and cardCheck(cardDeck[i+1:i+3])):
        getPoint += 2
    elif(card == 'K' and remaining >=3 and cardCheck(cardDeck[i+1:i+4])):
        getPoint += 3
    elif(card == 'A' and remaining >=4 and cardCheck(cardDeck[i+1:i+5])):
        getPoint += 4
    
    if(getPoint > 0 ):
        print(f'{playTurn} gets {getPoint}Points!')
    if(playTurn == 'A Player'):
        playerA_score += getPoint
        playTurn = 'B Player'
    else:
        playerB_score += getPoint
        playTurn = 'A Player'

print(f'A : {playerA_score} / B : {playerB_score}')