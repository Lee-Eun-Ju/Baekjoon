def solution(maps):
    
    n = len(maps)    #행
    m = len(maps[0]) #열
    
    # BFS : 큐 자료구조 사용
    from collections import deque
    queue = deque([(0,0)])    
    # answer = 0
    
    # 자리 이동 (이때 오른쪽 맨 밑으로 가는 것이 먼저 작동하도록)
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    
    while queue: # 큐가 빌 때까지 구현
        
        x,y = queue.popleft()
        # answer += 1
        
        # 도착한 경우
        if x==n-1 and y==m-1: 
            break
        
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
                
            if new_x<0 or new_x>(n-1) or new_y<0 or new_y>(m-1):
                continue        
            if maps[new_x][new_y] ==0:
                continue
            if maps[new_x][new_y] ==1:
                maps[new_x][new_y] = maps[x][y] + 1
                queue.append((new_x, new_y))

        
    # 도착하지 못한 경우
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]

    return answer

