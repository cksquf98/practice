import sys


dic = {}

N = int(sys.stdin.readline()) #가지고 있는 카드 갯수

cards = list(sys.stdin.readline().split())  #입력된 카드가 뭔지

for card in cards:
    if(dic.get(card)!= None and dic.get(card) > 0):
        dic[card] += 1
    else: 
        dic[card] = 1

M = int(sys.stdin.readline())
question_cards = list(sys.stdin.readline().split()) #갯수를 구해야 하는 카드

for q_card in question_cards:
    if(dic.get(q_card) == None): 
        print(0, end=' ')
    else:
        print(dic.get(q_card), end=' ')