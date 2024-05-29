'''
1학년 : 12불
2학년 : 10불
3학년 : 7불
4학년 : 5불
모인 돈의 50% -> 수학여행비 / 나머지 50% -> 브런치 비용
소수점 내림으로 인해 반영되지 않은 인원은 학생수가 가장 많은 학년에 추가하라

input : testcase{수학여행 비용, 학년 별 브런치 참여 비율, 브런치 참석 학생 수} 10개
output : 돈 더 마련해야 하면 YES, 아니면 NO 출력
'''
MONEY = [12, 10, 7, 5]
for i in range(1):
    cost = int(input('수학여행 비용 : '))
    grade1,grade2,grade3,grade4 = map(float, input('학년 별 참여 비율 : ').split())
    num = int(input('브런치 참여 학생 수 : '))



    # 학년 별 학생 수 = 비율 * 전체 학생수 => 소수점 내림으로 인해 총 학생수 != 학년 별 학생 수
    # 사라진 인원 파악이 필요함!!!
    students = []

    students.append(num * grade1)
    students.append(num * grade2)
    students.append(num * grade3)
    students.append(num * grade4)

    counted = sum(students)
    uncounted = num - counted

    # 소수점 내림으로 인해 반영되지 않은 인원은 학생수가 가장 많은 학년에 추가하라는 조건
    maxStudent = max(students) # 최댓값 반환
    where = students.index(maxStudent) # 최댓값의 인덱스 반환
    students[where] += uncounted


    total_cost = 0
    for i in range(4):
        total_cost += students[i] * MONEY[i] 


    if(total_cost/2 >= cost):
        print("ENOUGH!")
    else:
        print("NOT YET!")
