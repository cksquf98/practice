'''
수영장 운영시간 : 0~1000
인명구조원 1명 해고해야함

input : 파일 입력
(고용된 인명구조원 수 n / n명의 인명 구조원의 근무 시작시간 종료시간)

output : n-1명의 인명구조원의 최대 범위의 근무 시간 수
'''

def num_covered(timeTable, firedGuardNum):
    '''
    해고된 인명 구조원을 제외한 나머지 구조원들 근무시간 수 리턴
    근무 시작 종료시간 중복 불가라고 했으니까 set사용하기
    '''
    coveredTime = set()
    for i in range(len(timeTable)):
        if(i != firedGuardNum):
            t = timeTable[i]    
            for j in range(t[0],t[1]):
                coveredTime.add(j)      # 겹치는 시간 중복 제외하고, 커버되는 근무 시간이 집합에 추가됨

    return len(coveredTime)

input_file = open('lifeguards.in','r')
output_file = open('lifeguards.out','w')

timeTable = []
n = int(input_file.readline())
for i in range(n):
    t = input_file.readline().split()
    t[0] = int(t[0])
    t[1] = int(t[1])
    timeTable.append(t)

max_workingTime = 0
for firedGuard in range(n):
    workingTime = num_covered(timeTable,firedGuard)
    if(max_workingTime < workingTime):
        max_workingTime = workingTime

output_file.write(max_workingTime + '\n')
input_file.close()
output_file.close()