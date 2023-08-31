
N, M = map(int, input().split())

arr = [list(map(int,input().split())) for i in range(N)]
visited = [[-1] *(M) for i in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:        # 2는 하나이기 때문에, 시작점 지정
            cx, cy = i, j
            visited[i][j] = 0     # -1로 되있어서, 모든 값이 -1 되있는 걸 확인, 디버깅으로 시작 부분 값 0으로 수정
        elif arr[i][j] == 0:      # -1로 visited를 채웠기 때문에, 0인 부분은 0으로 수정
            visited[i][j] = 0

queue = [( cx , cy )]
 
while queue:                      # BFS
    x,y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny <M :
            if visited[nx][ny] == -1 or visited[nx][ny] == 0:   # 안가본 위치에서만 탐색.
                if arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

for i in range(N):
    print(*visited[i])