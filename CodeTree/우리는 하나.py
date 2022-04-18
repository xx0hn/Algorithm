# 우리는 하나
# n * n 크기의 격자로 이루어져 있는 나라의 정보가 주어집니다. 각 칸마다 하나의 도시가 있고, 각 도시마다의 높이 정보가 주어집니다. 이때 k개의 도시를 겹치지 않게 적절하게 골라, 골라진 k개의 도시로부터 갈 수 있는 서로 다른 도시의 수를 최대화 하고자 합니다. 이때 이동은 상하좌우로 인접한 도시간의 이동만 가능하며, 그 중에서도 두 도시간의 높이의 차가 u 이상 d 이하인 경우에만 가능합니다.

# k개의 도시를 적절하게 골라 갈 수 있는 서로 다른 도시의 수를 최대로 하는 프로그램을 작성해보세요. (시작 도시를 포함하여 셉니다)

# 입력 형식
# 첫 번째 줄에 격자의 크기를 나타내는 n과 고를 도시의 수를 나타내는 k 그리고 u, d 값이 각각 공백을 사이에 두고 주어집니다.

# 두 번째 줄 부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 순서대로 공백을 사이에 두고 주어집니다. (1 ≤ 입력으로 주어지는 숫자 ≤ 100)

# 1 ≤ n ≤ 8

# 1 ≤ k ≤ min(n, 3)

# 0 ≤ u ≤ d ≤ 100

# 출력 형식
# k개의 도시를 적절하게 골라 갈 수 있는 서로 다른 도시의 수 중 최댓값을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 1 2 3
# 1 2 3 
# 2 4 5
# 2 1 5
# 출력:

# 4
# 예제2
# 입력:

# 3 2 2 3
# 1 2 3
# 2 4 5
# 2 1 5
# 출력:

# 6
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
import sys
input=sys.stdin.readline
n, k, u, d=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
idxs=[]
for i in range(n):
    for j in range(n):
        idxs.append((i, j))
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
answer=0
combs=[]
def get_combs(cur, comb):
    if cur==len(idxs):
        if len(comb)==k:
            combs.append(comb)
        return
    if len(comb)>k:
        return
    get_combs(cur+1, comb+[idxs[cur]])
    get_combs(cur+1, comb)
def bfs(sy, sx):
    q=deque()
    q.append((sy, sx))
    visited[sy][sx]=1
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and u<=abs(grid[y][x]-grid[ny][nx])<=d and not visited[ny][nx]:
                visited[ny][nx]=1
                q.append((ny, nx))
get_combs(0, [])
for comb in combs:
    ans=0
    visited=[[0 for _ in range(n)] for _ in range(n)]
    for y, x in comb:
        bfs(y, x)
    for i in range(n):
        ans+=sum(visited[i])
    answer=max(answer, ans)
print(answer)
