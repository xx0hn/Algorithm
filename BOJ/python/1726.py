import collections
m, n=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(m)]
sy, sx, sd=map(int, input().split())
ey, ex, ed=map(int, input().split())
sy, sx, sd, ey, ex, ed=sy-1, sx-1, sd-1, ey-1, ex-1, ed-1
dy, dx=[0, 0, 1, -1], [1, -1, 0, 0]
def get_right_d(d):
    if d==0:
        return d+2
    if d==1:
        return d+2
    if d==2:
        return d-1
    if d==3:
        return d-3
def get_left_d(d):
    if d==0:
        return d+3
    if d==1:
        return d+1
    if d==2:
        return d-2
    if d==3:
        return d-2
def bfs(y, x, d):
    q=collections.deque()
    q.append((y, x, d, 0))
    visited=[[[False for _ in range(4)] for _ in range(n)] for _ in range(m)]
    visited[y][x][d]=True
    while q:
        y, x, d, cnt=q.popleft()
        if (y, x, d)==(ey, ex, ed):
            return cnt
        for i in range(1, 4):
            ny, nx, nd=y+i*dy[d], x+i*dx[d], d
            if 0<=ny<m and 0<=nx<n and not visited[ny][nx][nd]:
                if grid[ny][nx]==1:
                    break
                else:
                    visited[ny][nx][nd]=True
                    q.append((ny, nx, nd, cnt+1))
        ny1, nx1, nd1=y, x, get_right_d(d)
        if not visited[ny1][nx1][nd1]:
            visited[ny1][nx1][nd1]=True
            q.append((ny1, nx1, nd1, cnt+1))
        ny2, nx2, nd2=y, x, get_left_d(d)
        if not visited[ny2][nx2][nd2]:
            visited[ny2][nx2][nd2]=True
            q.append((ny2, nx2, nd2, cnt+1))
answer=bfs(sy, sx, sd)
print(answer)
