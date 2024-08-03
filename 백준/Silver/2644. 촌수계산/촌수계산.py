def DFS(n, ans):
    ans.append(n)
    if(not to_parent[n]):
        return ans
    
    p = to_parent[n][0]
    return DFS(p, ans)


if __name__=="__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    start, dest = map(int, input().split())

    to_parent = {i:[] for i in range(1,n+1)}
    visited = [False] * (n+1)

    m = int(input())
    for _ in range(m):
        parent, child = map(int, input().split())
        to_parent[child].append(parent)

    start_parent = DFS(start,[])
    dest_parent = DFS(dest, [])


    #공통 조상
    ancestor = -1

    #가장 맨 위 공통 조상부터 탐색하도록 역방향 돌리기
    start_parent.reverse()
    dest_parent.reverse()
    

    #반복문을 통해 가장 가까운 공통조상으로 마지막에 설정됨
    for s, d in zip(start_parent, dest_parent):
        if(s == d):
            #공통된 노드를 부모로 가지는 경우
            ancestor = s

        else:
            break

    

    if(ancestor == -1):
        print(ancestor)

    else:
        #순서 복원
        start_parent.reverse()
        dest_parent.reverse()

        print(start_parent.index(ancestor) + dest_parent.index(ancestor))