#3kg, 5kg 배수 아니니까 동전 문제처럼 큰거 우다다 쓰고 남은거 처리하는 방식으로는 안돼
#1. 3kg 봉지만 쓴 경우
#2. 5kg 봉지만 쓴 경우
#3. 섞어 쓴 경우

#정확하게 N킬로그램을 만들 수 없다면 -1을 출력
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())

    bongji_total = float('inf')

    # 나는 3개 케이스를 따로따로 보았는데, 아래에 한방에 하는 방법이 있었음
    # bongji_5KG = N//5
    # if(N % 5 == 0):
    #     bongji_total = min(bongji_total, bongji_5KG)
    
    # if(N % 3 == 0):
    #     bongji_total = min(bongji_total,N//3)
    
    # # print(bongji_total)
    # for i in range(1, bongji_5KG+1):
    #     N -= 5
    #     if(N % 3 == 0):
    #         bongji_total = min(bongji_total, i+(N//3))
    
    # 5kg 봉지를 사용하는 최대 개수에서 0까지 줄여가면서 3kg 봉지로 나누어 떨어지는지 확인
    for bongji_5KG in range(N // 5, -1, -1): 
        #봉지개수 = N//5 => 5kg봉지 최대 사용
        #봉지개수 = 0까지 돌아감 => 3kg 봉지만 사용 
        remaining_weight = N - (bongji_5KG * 5)
        if remaining_weight % 3 == 0:
            bongji_3KG = remaining_weight // 3
            bongji_total = min(bongji_total, bongji_5KG + bongji_3KG)

    
    if(bongji_total == float('inf')):
        print(-1)
    else:
        print(bongji_total)