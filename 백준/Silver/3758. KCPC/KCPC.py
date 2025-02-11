import sys
input = sys.stdin.readline
T = int(input())

def findAndUpdateScore(teamNum, questionNum, questionSubmit, newScore):
    questionList = questionSubmit[teamNum]
    for i in range(len(questionList)):
        question, score = questionList[i]
        if question == questionNum:
            if score < newScore:
                diff = newScore-score
                scoreAndCountAndLastSubmit[teamNum][0] += diff
                questionList[i][1] = newScore

            return

    questionSubmit[teamNum].append([questionNum, newScore])
    scoreAndCountAndLastSubmit[teamNum][0] += newScore

for _ in range(T):
    scoreAndCountAndLastSubmit = {}
    questionSubmit = {}
    totalTeam, K, myTeam, M = map(int, input().split(' ')) # 총 팀의 수, 문제 개수 K, 순위 구해야할 팀 아이디, 로그 엔트리 개수 M

    for i in range(1, M+1):
        teamNum, questionNum, score = map(int, input().split(' '))
        if teamNum in scoreAndCountAndLastSubmit:

            # 이미 제출한 문제라면 score 비교해서 갱신해야됨!!
            findAndUpdateScore(teamNum, questionNum, questionSubmit, score)
            scoreAndCountAndLastSubmit[teamNum][1] += 1
            scoreAndCountAndLastSubmit[teamNum][2] = i
        else:
            scoreAndCountAndLastSubmit[teamNum] = [score, 1, i]
            questionSubmit[teamNum] = [[questionNum, score]]

    rank = sorted(scoreAndCountAndLastSubmit.items(),
                  key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    for i in range(totalTeam):
        if rank[i][0] == myTeam:
            print(i+1)