def dfs (n):
    visited[n] = 1
    for x in arr[n]:
        if visited[x] == 0:
            dfs(x)

N = int(input())
Node = int(input())


arr = [[]for i in range(N+1)]

visited = [0] * (N+1)

for i in range(Node):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)
ans = sum(visited) - 1 # 최초 감염인 1은 제외

print(ans)