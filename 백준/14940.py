
N, M = map(int, input().split())

arr = [list(map(int,input().split())) for i in range(N)]
visited = [[-1] *(M) for i in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            cx, cy = i, j
            visited[i][j] = 0
        elif arr[i][j] == 0:
            visited[i][j] = 0

queue = [( cx , cy )]

while queue:
    x,y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny <M :
            if visited[nx][ny] == -1 or visited[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

for i in range(N):
    print(*visited[i])