# 바이러스 백신
# 실력체크
# 정답률 39% · 제출 140회 · 예상 소요 시간 65분

# 추천해요
# 아쉬워요
# ko-kr
# N*N 크기의 도시에 병원과 벽을 제외한 모든 지역에 바이러스가 생겼습니다. 비용상의 문제로 모든 병원에서 백신을 공급할 수는 없어, M개의 병원을 적절히 골라 최대한 빨리 바이러스를 없애려고 합니다.



# M개의 병원을 고르게 되면, 골라진 병원들을 시작으로 매 초마다 상하좌우로 인접한 지역 중 벽을 제외한 지역에 백신이 공급되기 때문에 그 자리에 있던 바이러스는 사라지게 됩니다.

# 예를 들어 위의 예에서 M = 3 일때 다음과 같이 병원을 고른 경우를 생각해봅시다.



# 1초 뒤 모습은 다음과 같습니다.



# 각 위치마다 바이러스가 사라지는 데 걸리는 시간을 적어보면 다음과 같습니다.



# 따라서 위의 예에서는 모든 바이러스가 사라지는 데 총 5초의 시간이 걸립니다.

# 하지만 만약 처음 주어진 예에서 다음과 같이 병원들을 골랐다면, 3초만에 모든 바이러스를 없앨 수 있게 됩니다.



# 이런 상황에서 M개의 병원을 적절히 골라 바이러스를 전부 없애는데 걸리는 시간 중 최소 시간을 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫째 줄에는 N과 M이 공백을 사이에 두고 주어집니다.

# 둘째 줄 부터는 N개의 줄에 걸쳐 각 행의 상태에 해당하는 N개의 숫자가 공백을 사이에 두고 주어집니다. 숫자는 0, 1, 2 중에 하나이며, 0은 바이러스, 1은 벽 그리고 2는 병원이 있음을 의미합니다. 입력으로 주어지는 총 병원의 수가 항상 M보다 크거나 같고, 10을 넘지 않습니다.

# 3 ≤ N ≤ 50

# 1 ≤ M ≤ 10

# 출력 형식
# M개의 병원을 적절히 골라 모든 바이러스를 없애는 데 필요한 최소 시간을 출력합니다. 만약 모든 바이러스를 없앨 수 있는 방법이 없다면 -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 6 3
# 2 1 2 0 1 1
# 0 0 0 1 0 1
# 1 1 0 0 2 0
# 1 0 0 1 0 1
# 1 0 0 0 0 1
# 1 1 2 1 0 1
# 출력:

# 3
# 예제2
# 입력:

# 4 1
# 0 1 0 2
# 0 1 1 0
# 2 0 1 0
# 0 0 1 0
# 출력:

# -1
# 예제3
# 입력:

# 3 1
# 1 1 2
# 2 1 2
# 1 1 1
# 출력:

# 0
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
import copy
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 0, -1, 1], [1, -1, 0, 0]
hospitals=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            hospitals.append((i, j))
combs=[]
def get_combs(cur, comb):
    if cur==len(hospitals):
        if len(comb)==m:
            combs.append(comb)
        return
    if len(comb)>m:
        return
    get_combs(cur+1, comb+[hospitals[cur]])
    get_combs(cur+1, comb)
def heal(y, x, grid):
    q=deque()
    q.append((y, x))
    time[y][x]=0
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and time[ny][nx]>time[y][x]+1 and grid[ny][nx]!=1:
                time[ny][nx]=time[y][x]+1
                q.append((ny, nx))
def get_max():
    result=0
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                result=max(result, time[i][j])
    return result
answer=1e9
get_combs(0, [])
for comb in combs:
    tmp=copy.deepcopy(grid)
    time=[[1e9 for _ in range(n)] for _ in range(n)]
    for y, x in comb:
        heal(y, x, tmp)
    answer=min(answer, get_max())
if answer==1e9:
    print(-1)
else:
    print(answer)
