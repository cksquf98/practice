def solution(queue1, queue2):
    """
    한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주
    
    두 합을 같게 만드려면
    1. queue중에서 더 적은 합을 가지고있는 애를 봐 -> queue1으로 가정
    2. queue1에서 pop -> queue2에 넣넣
    3. 큐1,2의 sum 비교
    
    근데 합을 같게 못만드는 경우 종료 조건을 어떻게 잡아야 하지?!?!
    """
    
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    total_len = len(queue1)+len(queue2)
    answer = -1
    
    cnt = 0
    """
    틀렸던 부분 : 
    1. while문 종료 조건
    한 큐에서 다른 큐로 원소를 옮기는 과정에서 모든 원소를 다 옮기고 다시 되돌려도 합이 같아지지 않으면, 더 이상 방법이 없는 것!!!!
    => 종료 조건은 따라서 cnt가 (len(queue1)+len(queue2))*2보다 커지는 경우겠다잉
    => 근데 그냥 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000 이 조건에 따라서 300000으로 해도 정답이였네
    
    2. sum 계산하는 부분 <<여기서 시간초과가 났었던거군
    슬라이딩 윈도우를 활용하지 않았더니 시간초과가 계속 났음
    """
    while cnt <= (total_len)*2:
        diff = abs(sum1 - sum2)
        
        if(sum1 > sum2):
            elem = queue1.popleft()
            queue2.append(elem)
            sum1 -= elem
            sum2 += elem
            cnt += 1
        elif (sum1 < sum2):
            elem = queue2.popleft()
            queue1.append(elem)
            sum2 -= elem
            sum1 += elem
            cnt += 1
        else:
            answer = cnt
            break
            
    
    return answer
