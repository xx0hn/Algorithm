# 빙하
# N*M 크기의 격자안에 빙하의 정보가 주어집니다. 격자의 가장 바깥 부분은 항상 빙하가 아니고, 빙하를 제외한 나머지 위치에는 전부 물이 채워져 있습니다. 숫자 1은 빙하를, 숫자 0은 물을 나타냅니다.



# 빙하는 1초에 한 번씩 물에 닿아있는 부분들이 동시에 녹습니다. 하지만 빙하로 둘러쌓여있는 물의 경우에는 붙어있는 빙하를 녹이지 못합니다. 여기서 닿아있다는 말은 상하좌우로 인접한 경우를 의미하며, 다음의 경우 역시 안쪽에 있는 0들은 빙하로 둘러쌓인 것이기 때문에 빙하가 녹는데 영향을 주지 못합니다.



# 맨 위에서 주어진 예시의 경우 안쪽에 있는 0은 빙하로 둘러쌓여 있으므로 바깥쪽에 있는 0만이 빙하가 녹는데 영향을 미칩니다.



# 빙하가 전부 녹는데 걸리는 시간과 마지막으로 녹은 빙하의 크기(1의 개수)를 구하는 프로그램을 작성해보세요.

# 위의 예에서는 빙하가 녹는데 2초의 시간이 소요되며, 마지막으로는 크기가 4인 빙하가 녹으며 전부 없어지게 됩니다.



# 입력 형식
# 첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어지고, 두 번째 줄부터는 N개의 줄에 걸쳐 각 행에 위치한 M개의 숫자가 공백을 사이에 두고 주어집니다. 입력으로 주어지는 초기 빙하의 크기가 1 이상이라 가정해도 좋습니다.

# 3 ≤ N ≤ 200

# 3 ≤ M ≤ 200

# 출력 형식
# 빙하가 전부 녹는데 걸리는 시간과, 마지막으로 녹은 빙하의 크기를 공백을 사이에 두고 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3 3
# 0 0 0
# 0 1 0
# 0 0 0
# 출력:

# 1 1
# 예제2
# 입력:

# 6 7
# 0 0 0 0 0 0 0
# 0 1 1 1 1 0 0
# 0 1 1 0 1 1 0
# 0 1 0 1 1 1 0
# 0 1 1 1 1 1 0
# 0 0 0 0 0 0 0
# 출력:

# 2 4
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
from copy import deepcopy
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def bfs(sy, sx):
    q=deque()
    q.append((sy, sx))
    visited[sy][sx]=1
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if grid[ny][nx]==1:
                    tmp[ny][nx]=0
                if grid[ny][nx]==0 and not visited[ny][nx]:
                    visited[ny][nx]=1
                    q.append((ny, nx))
cnt=0
ices=[]
while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    cnt+=1
    ice=0
    for i in range(n):
        ice+=sum(grid[i])
    if ice==0:
        break
    else:
        ices.append((cnt, ice))
    tmp=deepcopy(grid)
    bfs(0, 0)
    grid=deepcopy(tmp)
print(*ices[-1])
