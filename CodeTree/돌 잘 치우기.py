# 돌 잘 치우기
# 숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, 주어진 돌 중 m개의 돌만 적절하게 치워 k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 최대로 하는 프로그램을 작성해보세요. 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 돌이 있어 해당 칸이 이동할 수 없는 곳임을 의미합니다.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 시작점의 수를 나타내는 k, 그리고 꼭 치워야 할 돌의 개수 m이 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 그 다음 줄 부터는 k개의 줄에 걸쳐 각 시작점의 위치 (r, c)가 공백을 사이에 두고 주어집니다. (r, c)는 r행 c열 위치가 시작점 중 하나임을 의미합니다. 모든 시작점의 위치에 적혀있는 숫자는 0이고, 시작점끼리 서로 겹치지 않게 주어진다고 가정해도 좋습니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n)

# 3 ≤ n ≤ 100

# 1 ≤ k ≤ n * n

# 0 ≤ m ≤ 입력으로 주어지는 초기 돌의 개수 ≤ 8

# 출력 형식
# 주어진 돌 중 m개의 돌을 적절하게 치웠을 때 시작지점으로부터 방문이 가능한 서로 다른 칸의 수의 최댓값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 2 1
# 0 0 0
# 0 0 1
# 1 0 0
# 1 1
# 1 2
# 출력:

# 8
# 예제2
# 입력:

# 4 2 2
# 0 1 1 0
# 0 1 1 0
# 0 1 1 1
# 0 1 0 0
# 1 4
# 4 4
# 출력:

# 10
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import itertools
import copy
import collections
n, k, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
s=[list(map(int, input().split())) for _ in range(k)]
dy, dx=[1, 0, -1, 0], [0, 1, 0, -1]
rocks=[]
answer=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            rocks.append((i, j))
def bfs(sy, sx, tmp_grid):
    visited[sy][sx]=1
    q=collections.deque()
    q.append((sy, sx))
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and tmp_grid[ny][nx]!=1:
                visited[ny][nx]=1
                q.append((ny, nx))
cases=list(itertools.combinations(rocks, m))
for i in range(len(cases)):
    tmp_grid=copy.deepcopy(grid)
    visited=[[0 for _ in range(n)] for _ in range(n)]
    result=0
    for j in range(m):
        tmp_grid[cases[i][j][0]][cases[i][j][1]]=0
    for j in range(k):
        bfs(s[j][0]-1, s[j][1]-1, tmp_grid)
    for j in range(n):
        result+=sum(visited[j])
    answer=max(answer, result)
print(answer)
