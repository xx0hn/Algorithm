# 방화벽 설치하기
# 실력체크
# 정답률 27% · 제출 486회 · 예상 소요 시간 55분

# 추천해요
# 아쉬워요
# ko-kr
# n * m 크기의 이차원 영역에 방화벽을 설치하여 불로 인한 피해를 최소화 하고자 합니다. 불은 상하좌우의 인접한 공간으로 모두 번지는 특성을 지니고 있으며, 방화벽을 뚫을 수는 없습니다. 예를 들어 [그림 1]과 같이 불과 방화벽이 배치되어 있을 경우, 불이 모두 번지고 난 후에는 [그림 2]와 같은 상태로 변하게 됩니다. 기존에 이미 설치되어 있는 방화벽을 제외하고 추가로 3개의 방화벽을 설치할 수 있을 때 정확히 3개의 방화벽을 추가로 설치하여 불이 퍼지지 않는 영역이 최대일 때의 크기를 출력하는 코드를 작성해보세요. 단, 방화벽을 불이 있는 위치에 설치할 수는 없습니다.



# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고,

# 두 번째 줄부터 (n+1)번째 줄까지는 각 행에 불이 있는 경우 2, 방화벽이 있는 경우 1, 빈 칸인 경우 0이 입력으로 공백을 사이에 두고 주어집니다.

# 3 ≤ n, m ≤ 8

# 2 ≤ 총 불의 개수 ≤ 10

# 3 ≤ 총 빈 칸의 개수

# 출력 형식
# 방화벽 3개를 추가로 설치 했을 때 방화벽을 제외하고 불이 퍼지지 않는 영역 크기의 최댓값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 4
# 0 0 0 0
# 0 2 0 0
# 0 0 0 2
# 출력:

# 2
# 예제2
# 입력:

# 5 5
# 2 1 0 0 0
# 0 1 0 1 1
# 1 0 1 2 0
# 0 0 1 0 0
# 0 1 0 0 0
# 출력:

# 12
# 예제 설명
# 예제 1에서는 1행 2열, 2행 3열, 2행 4열에 방화벽을 추가로 설치하면 불이 퍼지지 않는 2개의 영역을 얻게 됩니다.

# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
import copy
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
idxs=[]
for i in range(n):
    for j in range(m):
        if grid[i][j]==0:
            idxs.append((i, j))
dy, dx=[0, 0, -1, 1], [1, -1, 0, 0]
cases=[]
def get_cases(cur, case):
    if cur==len(idxs):
        if len(case)==3:
            cases.append(case)
        return
    if len(case)>3:
        return
    get_cases(cur+1, case+[idxs[cur]])
    get_cases(cur+1, case)
def get_safe(grid):
    result=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                result+=1
    return result
def bfs(y, x, grid):
    q=deque()
    q.append((y, x))
    visited[y][x]=True
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m and grid[ny][nx]!=1 and not visited[ny][nx]:
                visited[ny][nx]=True
                grid[ny][nx]=2
                q.append((ny, nx))
get_cases(0, [])
answer=0
for case in cases:
    tmp_grid=copy.deepcopy(grid)
    visited=[[False for _ in range(m)] for _ in range(n)]
    for y, x in case:
        tmp_grid[y][x]=1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2 and not visited[i][j]:
                bfs(i, j, tmp_grid)
    answer=max(answer, get_safe(tmp_grid))
print(answer)
