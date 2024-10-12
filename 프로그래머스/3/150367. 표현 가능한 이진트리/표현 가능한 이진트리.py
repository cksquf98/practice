def search(number):
    length = len(number)  # 이진수 문자열의 길이를 구함
    # 길이가 1이거나, 문자열에 '1'이 없거나, '0'이 없으면 True 반환
    if length == 1 or '1' not in number or '0' not in number:
        return True  # 기저 사례: 길이가 1이거나, 모두 0 또는 모두 1인 경우는 유효함
    
    mid = length // 2  # 문자열의 중간 인덱스를 계산
    # 중간 위치의 값이 '0'인 경우 False 반환
    if number[mid] == '0':
        return False  # 중간 값이 0이면 조건을 만족하지 않음
    
    # 재귀적으로 왼쪽 및 오른쪽 부분 문자열을 검사하여 둘 다 True인 경우에만 True 반환
    return search(number[:mid]) and search(number[mid + 1:])

def solution(numbers):
    # 주어진 숫자들을 이진수 문자열로 변환하고, '0b' 접두사를 제거
    bin_numbers = [bin(x)[2:] for x in numbers]
    # 최대 길이를 기준으로 (0부터 49까지) 각 이진수 문자열의 최대 길이 -1 값을 포함하는 리스트를 생성
    bin_list = [2**x - 1 for x in range(50)]
    answer = []  # 결과를 저장할 리스트
    
    # 각 이진수 문자열에 대해
    for number in bin_numbers:
        length = len(number)  # 현재 이진수 문자열의 길이
        
        # 길이를 맞추기 위해 0으로 패딩할 최대 길이를 결정
        for num in bin_list:
            if num >= length:
                number = '0' * (num - length) + number  # 왼쪽에 0을 추가하여 길이를 맞춤
                break  # 조건에 맞는 길이를 찾으면 반복 종료
        
        # search 함수를 사용하여 유효성 검사, 유효하면 1, 그렇지 않으면 0을 추가
        answer.append(1 if search(number) else 0)
    
    return answer  # 최종 결과 리스트 반환
