# 갈 수 있는 곳들
# 숫자 0, 1로만 이루어진 n * n 격자가 주어졌을 때, k개의 시작점으로부터 상하좌우 인접한 곳으로만 이동하여 도달 가능한 칸의 수를 구하는 프로그램을 작성해보세요. 숫자 0은 해당 칸이 이동할 수 있는 곳임을, 숫자 1은 해당 칸이 이동할 수 없는 곳임을 의미합니다.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n과 시작점의 수를 나타내는 k 값이 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다.

# 그 다음 줄 부터는 k개의 줄에 걸쳐 각 시작점의 위치 (r, c)가 공백을 사이에 두고 주어집니다. (r, c)는 r행 c열 위치가 시작점 중 하나임을 의미합니다. 모든 시작점의 위치에 적혀있는 숫자는 0이고, 시작점끼리 서로 겹치지 않게 주어진다고 가정해도 좋습니다. (1 ≤ r ≤ n, 1 ≤ c ≤ n)

# 1 ≤ n ≤ 100

# 1 ≤ k ≤ n * n

# 출력 형식
# 시작지점으로부터 방문이 가능한 서로 다른 칸의 수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 2
# 0 0 0
# 0 0 1
# 1 0 0
# 1 1
# 1 2
# 출력:

# 7
# 예제2
# 입력:

# 4 2
# 0 1 0 0
# 0 1 0 0
# 0 1 1 1
# 0 1 0 0
# 1 4
# 4 4
# 출력:

# 6
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
n, k=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
s=[list(map(int, input().split())) for _ in range(k)]
visited=[[0 for _ in range(n)] for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1 ,0]
def bfs(sy, sx):
    q=deque()
    q.append((sy, sx))
    visited[sy][sx]=1
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and not grid[ny][nx]:
                visited[ny][nx]=1
                q.append((ny, nx))
for y, x in s:
    bfs(y-1, x-1)
answer=0
for i in range(n):
    answer+=sum(visited[i])
print(answer)
