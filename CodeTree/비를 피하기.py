# 비를 피하기
# 숫자 0, 1, 2, 3로만 이루어진 n * n 격자에서 사람이 h명 겹치지 않게 서 있고, 비를 피할 수 있는 공간의 위치 m개가 주어졌을 때 각 사람마다 비를 피할 수 있는 가장 가까운 공간까지의 거리를 구하는 프로그램을 작성해보세요. 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 벽이 있어 해당 칸이 이동할 수 없는 곳임을 의미합니다. 숫자 2는 해당 칸에 사람이 서있음을 의미하고, 숫자 3는 해당 공간이 비를 피할 수 있는 공간임을 의미합니다. 사람은 상하좌우 인접한 곳으로만 움직 일 수 있으며 한 칸 움직이는 데 정확히 1초가 소요됩니다. 벽이 아닌 곳은 전부 이동이 가능합니다.

# 입력 형식
# 첫 번째 줄에 격자의 크기를 나타내는 n과 사람의 수를 나타내는 h 그리고 비를 피할 수 있는 공간의 수를 나타내는 m이 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 2 ≤ n ≤ 100

# 1 ≤ h ≤ n * n

# 1 ≤ m ≤ n * n

# 출력 형식
# n개의 줄에 걸쳐 각 행마다 각 칸에 대한 정보를 공백을 사이에 두고 출력합니다. 만약 해당 칸이 사람이 있던 칸이 아니라면 0을 출력하고, 사람이 있던 칸이라면 해당 사람이 비를 피할 수 있는 공간까지 가는데 걸리는 최소시간을 출력합니다. 만약 해당 위치에 있는 사람이 절대 비를 피할 수 없다면 -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 1 1
# 1 2 0
# 3 1 0
# 0 0 0
# 출력:

# 0 6 0
# 0 0 0
# 0 0 0
# 예제2
# 입력:

# 4 5 2
# 1 2 0 1
# 3 1 1 2
# 2 1 2 0
# 2 0 0 3
# 출력:

# 0 -1 0 0
# 0 0 0 2
# 1 0 2 0
# 2 0 0 0
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
n, h, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
humans=[]
safe=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            humans.append((i, j))
        if grid[i][j]==3:
            safe.append((i, j))
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def bfs(human):
    sy, sx=human
    q=deque()
    q.append((sy, sx, 0))
    visited=[[False for _ in range(n)] for _ in range(n)]
    visited[sy][sx]=True
    while q:
        y, x, time=q.popleft()
        if (y, x) in safe:
            return time
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and grid[ny][nx]!=1 and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny, nx, time+1))
    return -1
answer=[[0 for _ in range(n)] for _ in range(n)]
for human in humans:
    answer[human[0]][human[1]]=bfs(human)
for i in range(n):
    print(*answer[i])
