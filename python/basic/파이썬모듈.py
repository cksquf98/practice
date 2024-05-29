import random
print(random.randint(1,5))          #[a,b]사이 값 랜덤 선택
print(random.choice(['Yes','No']))  #후보중 랜덤으로 하나 선택

from random import randint
randint(2,10)

from bisect import bisect_left, bisect_right

#bisect_ : 오름차순으로 정렬된 리스트와 값 X를 제공하여 함수 호출
print(bisect_left([1,1,2,3,3,4,4,5,6],4))    #값 4를 가지는 가장 왼쪽의 인덱스 반환 -> 5
print(bisect_right([1,1,2,3,3,4,4,5,6],4))  #값 4보다 큰 첫번째 녀석(오른쪽)의 인덱스를 반환

print(bisect_left([1,3,4,5,6],2))         #값이 리스트에 없으면 X보다 더 큰 값들 중 첫번째 값의 인덱스 반환 -> 1
bisect_left([1,3,4,5,6],100)          #값X가 리스트 모든 값보다 큰 값이면 리스트 길이 반환 -> 5