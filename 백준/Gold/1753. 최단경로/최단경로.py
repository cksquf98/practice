"""

* HeapQueue를 이용하면 최솟값을 빼내는데 O(log N) 복잡도로 줄어듬 <<우선순위 큐>>
  heapq: minHeap에서 최솟값을 가장 먼저 pop

1. 우선순위 큐 사용 -> start 노드번호와 비용 넣어주기
2. heappop으로 노드 뽑아서 current로 설정 -> 인접리스트에서 current 노드의 인접노드들을 큐에 넣기
3. (current노드까지의 비용 + heappop으로 뽑은 인접 노드로 가는데의 비용)과 기존 저장된 비용을 비교
4. 더 작은 값을 distances에 저장
5. 최소 비용의 인접 노드를 큐에 넣기 
-> 큐가 비게 될 때까지 반복

"""


def Dijstra(start):
    import heapq

    distance = [INF] * (V+1)
    priority_q = []
    
    distance[start] = 0 #자기 자신과의 거리는 0
    heapq.heappush(priority_q, (0, start))

    while priority_q: #큐가 비면 갈 수 있는 인접노드가 없다는 뜻
        dist, current = heapq.heappop(priority_q)


        #인접노드 최소비용 구하기
        for to_v, weight in graph[current]:
            to_v_cost = dist + weight

            if(to_v_cost < distance[to_v]):
                distance[to_v] = to_v_cost
                heapq.heappush(priority_q,(to_v_cost,to_v))

    
    return distance



if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    INF = 100000000 #가중치만 보는게 아니고 총 비용이 저장되는 배열이니까 11로 두면 안됐네 헤헤

    V, E = map(int, input().split())
    graph = {node:[] for node in range(1, V+1)}

    start = int(input())

    for _ in range(E):
        from_v, to_v, weight = map(int, input().split())
        graph[from_v].append((to_v, weight))
    
    
    distance = Dijstra(start)

    for i in range(1,V+1):
        if(distance[i] == INF):
            print("INF")
        else:
            print(distance[i])

    