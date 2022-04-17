# k개의 벽 없애기
# 숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, k개의 벽을 적절하게 없애 시작점으로부터 상하좌우 인접한 곳으로만 계속 이동하여 도착점까지 도달하는 데 걸리는 시간을 최소로 하는 프로그램을 작성해보세요. 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 벽이 있어 해당 칸이 이동할 수 없는 곳임을 의미합니다. 한 칸을 이동하는 데에는 정확히 1초의 시간이 소요됩니다.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 없애야 할 벽의 개수 k가 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 그 다음 줄에는 시작점의 위치 (r1, c1)과 도착점의 위치 (r2, c2)가 각각 공백을 사이에 두고 주어집니다. 이는 r1행 c1열에서 출발하여 r2행 c2열로 도착해야 함을 의미합니다. 시작 위치와 도착 위치에는 항상 숫자 0이 주어진다고 가정해도 좋습니다.

# 3 ≤ n ≤ 100

# 0 ≤ k ≤ 입력으로 주어지는 초기 벽의 개수 ≤ 8

# 출력 형식
# k개의 벽을 적절하게 없앴을 때 시작점에서 도착점까지 이동하는 데 걸리는 최소 시간을 출력합니다. 만약 k개의 벽을 어떻게 없애도 도착점까지 도달하는 것이 불가능하다면, -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 2
# 0 0 0 0
# 0 1 1 1
# 1 1 1 1
# 0 1 0 0
# 1 1
# 4 4
# 출력:

# 6
# 예제2
# 입력:

# 4 2
# 0 1 0 0
# 1 0 0 1
# 0 0 1 1
# 0 1 1 0
# 1 1
# 4 4
# 출력:

# -1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
from copy import deepcopy
from sys import maxsize
n, k=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
r1, c1=map(int, input().split())
r2, c2=map(int, input().split())
r1, c1, r2, c2=r1-1, c1-1, r2-1, c2-1
answer=maxsize
walls=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            walls.append((i, j))
dr, dc=[0, 1, 0, -1], [1, 0, -1, 0]
cases=[]
def break_wall(cur, result):
    if cur==len(walls):
        if len(result)==k:
            cases.append(result)
        return
    break_wall(cur+1, result+[walls[cur]])
    break_wall(cur+1, result)
def bfs(grid):
    q=deque()
    q.append((r1, c1, 0))
    visited=[[False for _ in range(n)] for _ in range(n)]
    visited[r1][c1]=True
    while q:
        r, c, cnt=q.popleft()
        if (r, c)==(r2, c2):
            return cnt
        for i in range(4):
            nr, nc=r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0 and not visited[nr][nc]:
                visited[nr][nc]=True
                q.append((nr, nc, cnt+1))
    return -1
break_wall(0, [])
for case in cases:
    tmp_grid=deepcopy(grid)
    for idx in case:
        tmp_grid[idx[0]][idx[1]]=0
    tmp=bfs(tmp_grid)
    if tmp==-1:
        continue
    answer=min(answer, bfs(tmp_grid))
if answer==maxsize:
    answer=-1
print(answer)
