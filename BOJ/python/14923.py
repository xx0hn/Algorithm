# 문제
# 홍익이는 사악한 마법사의 꾐에 속아 N x M 미로 (Hx, Hy) 위치에 떨어졌다. 다행히도 홍익이는 마법사가 만든 미로의 탈출 위치(Ex, Ey)를 알고 있다. 하지만 미로에는 곳곳에 마법사가 설치한 벽이 있어 홍익이가 탈출하기 어렵게 하고 있다.
#
# 홍익이는 마법사의 연구실에서 훔친 지팡이가 있어, 벽을 길로 만들 수 있다. 그렇지만, 안타깝게도 마법의 지팡이는 단 한 번만 사용할 수 있다.
#
# 이때, 홍익이를 도와 미로에서 탈출할 수 있는지 알아보고, 할 수 있다면 가장 빠른 경로의 거리 D는 얼마인지 알아보자.
#
# 인접한 칸으로 이동하는데 똑같은 시간이 들고, 벽을 부수는 데 시간이 걸리지 않는다.
#
# 입력
# N M
# Hx Hy
# Ex Ey
# N X M 행렬
# 2 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
# 1 ≤ Hx, Hy, Ex, Ey ≤ 1000
# (Hx, Hy)≠ (Ex, Ey)
# 행렬은 0과 1로만 이루어져 있고, 0이 빈 칸, 1이 벽이다.
# 출력
# D (탈출 할 수 없다면, -1을 출력한다.)
import collections
n, m=map(int, input().split())
hy, hx=map(int, input().split())
ey, ex=map(int, input().split())
hy, hx, ey, ex=hy-1, hx-1, ey-1, ex-1
grid=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def bfs(y, x):
    q=collections.deque()
    q.append((y, x, 0, 1))
    visited=[[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[y][x][1]=True
    while q:
        y, x, cnt, magic=q.popleft()
        if (y, x)==(ey, ex):
            return cnt
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if visited[ny][nx][magic]:
                    continue
                if grid[ny][nx]==1 and magic==1:
                    visited[ny][nx][0]=True
                    q.append((ny, nx, cnt+1, magic-1))
                elif grid[ny][nx]==0:
                    visited[ny][nx][magic]=True
                    q.append((ny, nx, cnt+1, magic))
    return -1
print(bfs(hy, hx))
