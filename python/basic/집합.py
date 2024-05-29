'''
<이메일 주소 정리>
1. 전체 대소문자 구분X
2. @ 앞 점(.) 무시
3. + 뒤 ~ @ 앞 문자 무시

이메일 주소 입력 > 필터링 진행 시 동일 주소면 고유 이메일 주소 아님

output : 이메일 고유 주소 개수
'''
def cleanEmail(email):
    # 1번 정리
    email = email.lower()

    # 3번 정리
    plus_index = email.find('+')
    address_index = email.find('@')

    if(plus_index != -1):
        email = email[:plus_index]+email[address_index:]

    # 2번 정리
    cleanedEmail =''
    address_index = email.find('@')
    for i in range(address_index):
        if(email[i] !='.'):
            cleanedEmail += email[i]
    cleanedEmail += email[address_index:]
    return cleanedEmail


n = int(input('email num : '))
addresses = []
for i in range(n):
    email = input(f'Enter your unique email : ')
    email = cleanEmail(email)
    if email not in addresses:
        addresses.append(email)
print(len(addresses))

'''
리스트
in 연산 탐색 : 시간복잡도 O(n)
애초에 중복을 제거해주는 Set를 사용해보자! 집합에서 수행하는 연산이 더 빠르다!
'''
n = int(input('email num : '))
addresses_set = set()
for i in range(n):
    email = input(f'Enter your unique email : ')
    email = cleanEmail(email)
    addresses_set.add(email) # in 연산 쓸 필요 없음
print(len(addresses))


# 집합은 순서 지맘대로, 인덱싱/슬라이싱 불가
s = {5,1,2,2,2,4,10,18,41}
#print(s[0]) : XXX


# 집합 안 리스트 저장 불가 <-> 리스트 안 집합 저장 가능
l = [{1,2},{3,4}]
print(l[0])