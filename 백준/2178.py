# 최단 거리 -> bfs

N, M = map(int,input().split())

arr = [list(map(int,input())) for i in range(N)]
visited = [[0] *(M) for i in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = [(0,0)]
visited[0][0] = 1
while queue:
    x,y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny <M and visited[nx][ny] == 0:
            if arr[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

print(visited[N-1][M-1])