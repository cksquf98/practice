def DFS(current,visited):
    visited[current] = True
    print(current, end = ' ')
    for index in vertex[current]:
        if(index not in visited):
            DFS(index, visited)
            
    

def BFS(current):
   
    visited = {}
    
    queue = [current]
    visited[current] = True
    
    while(len(queue) > 0):
        current = queue.pop(0)
        visited[current] = True
        print(current, end=' ')
        
        for index in vertex[current]:
            if(index not in visited):
                queue.append(index)
                visited[index] = True
    
        


if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    
    N, M, V = map(int, input().rstrip().split())
    
    vertex = {i:[] for i in range(1, N+1)}
   
    
    for i in range(1,M+1):
        v1, v2 = map(int,input().split())
        vertex[v1].append(v2)
        vertex[v2].append(v1)
        
    for key in vertex:
        vertex[key].sort()            
    
    DFS(V, {})
    print()
    BFS(V)        
    