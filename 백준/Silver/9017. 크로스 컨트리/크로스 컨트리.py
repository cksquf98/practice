import sys
input = sys.stdin.readline

# 조건 1. 6명의 팀원
# 조건 2. 팀 점수 = 상위 4명의 점수 합
# 조건 3. 팀 점수가 동점이라면 5번째 주자의 점수로 결정
# 조건 4. 점수가 낮은 팀이 승리
# 우승팀의 번호를 출력하시오!

T = int(input())
for _ in range(T):
    N = int(input())
    raceResult = list(map(int, input().split(' ')))
    result = {}

    teamList = set(raceResult)

    member = {}

    for result in raceResult:
        if member.get(result) != None:
            member[result] += 1
        elif member.get(result) == None:
            member[result] = 1

    for team in member.keys():
        if member[team] < 6:
            teamList.remove(team)

    raceResult = [
        team for team in raceResult if team in teamList]  # 리스트 축약으로 6명 미만 팀 제거

    teamScore = {team: [] for team in teamList}
    for i in range(len(raceResult)):
        teamScore[raceResult[i]].append(i)

    winningTeam = -1
    minScore = float('inf')
    for team in teamList:
        score = sum(teamScore[team][:4])

        if score < minScore:
            winningTeam = team
            minScore = score
        elif score == minScore:
            if teamScore[winningTeam][4] > teamScore[team][4]:
                winningTeam = team

    print(winningTeam)