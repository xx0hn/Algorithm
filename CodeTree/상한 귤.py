# 상한 귤
# 숫자 0, 1, 2로만 이루어진 n * n 격자에서 0초에 k개의 상한 귤로부터 시작하여 1초에 한 번씩 모든 상한 귤로부터 인접한 곳에 있는 귤이 동시에 전부 상하게 될때, 각 귤마다 최초로 상하게 되는 시간을 구하는 프로그램을 작성해보세요. 숫자 0은 해당 칸에 아무것도 놓여있지 않음을, 숫자 1은 해당 칸에 귤이 놓여있음을, 숫자 2는 해당 칸에 상한 귤이 처음부터 놓여 있음을 의미합니다.

# 입력 형식
# 첫 번째 줄에 격자의 크기를 나타내는 n과 초기에 상해있는 귤의 수를 나타내는 k가 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 2 ≤ n ≤ 100
# 1 ≤ k ≤ n * n
# 출력 형식
# n개의 줄에 걸쳐 각 행마다 각 칸에 대한 정보를 공백을 사이에 두고 출력합니다. 만약 처음부터 비어있던 칸이라면 -1을 출력합니다. 처음에 귤이 들어있던 칸이라면 상하는 데 까지 걸리는 시간을 출력합니다. 만약 끝까지 상하지 않는 귤이라면 -2를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 1
# 1 1 1
# 1 0 1
# 1 0 2
# 출력:

# 4 3 2
# 5 -1 1
# 6 -1 0
# 예제2
# 입력:

# 4 2
# 0 0 1 0
# 1 1 1 2
# 0 2 1 0
# 0 0 0 1
# 출력:

# -1 -1 2 -1
# 2 1 1 0
# -1 0 1 -1
# -1 -1 -1 -2
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
n, k=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
s=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            s.append((i, j))
visited=[[-1 for _ in range(n)] for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def bfs(sy, sx):
    q=deque()
    q.append((sy, sx))
    visited[sy][sx]=0
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and grid[ny][nx]==1 and (visited[ny][nx]==-1 or visited[ny][nx]>visited[y][x]+1):
                visited[ny][nx]=visited[y][x]+1
                q.append((ny, nx))
for y, x in s:
    bfs(y, x)
for i in range(n):
    for j in range(n):
        if visited[i][j]==-1 and grid[i][j]==1:
            visited[i][j]=-2
for i in range(n):
    print(*visited[i])
