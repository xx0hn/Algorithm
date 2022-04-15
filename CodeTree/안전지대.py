# 안전 지대
# N*M 크기의 격자로 구성된 마을이 있습니다. 격자마다 한 집을 의미하며, 각 집의 높이는 1에서 100 사이의 숫자로 이루어져 있습니다.



# 이런 상황에서 만약 비가 K (K >= 1)만큼 온다고 한다면, 마을에 있는 집들 중 높이가 K 이하인 집들은 전부 물에 잠기게 되기 때문에, 대책을 세우기 위해 미리 각 K에 따라 안전 영역의 개수가 어떻게 달라지는지를 보려고 합니다. 여기서 안전 영역이란 잠기지 않은 집들로 이루어져 있으며, 잠기지 않은 집들끼리 서로 인접해 있는 경우 동일한 안전 영역에 있는 것으로 봅니다.

# 위의 예에서 K = 1인 경우에는 안전한 영역은 1개 입니다.



# K = 3 인 경우에는 안전 영역의 수가 3이 되며



# K = 4 일때는 안전 영역의 수가 4가 됩니다.



# 이런 상황에서 안전 영역의 수가 최대가 될때의 K와 그때의 안전 영역의 수를 구해주는 프로그램을 작성해보세요.

# 위의 예에서는 K = 4일때 안전 영역의 수가 4로 최대가 됩니다.



# 입력 형식
# 첫 번째 줄에는 N과 M이 공백을 사이에 두고 주어지고,

# 두 번째 줄부터는 N개의 줄에 걸쳐 각 행에 위치한 M개의 마을의 높이 정보가 공백을 사이에 두고 주어집니다.

# 1 ≤ N ≤ 50

# 1 ≤ M ≤ 50

# 출력 형식
# 1 이상의 K 중, 안전 영역의 수가 최대가 될때의 K와 그 때의 안전 영역의 수를 공백을 사이에 두고 출력합니다. 만약 안전 영역의 수가 최대가 되는 K가 여러 개라면, 그 중 가장 작은 K를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 4 5
# 1 2 4 7 5
# 4 2 5 5 2
# 5 7 3 2 6
# 6 7 4 5 1
# 출력:

# 4 4
# 예제2
# 입력:

# 3 2
# 1 2
# 2 2
# 1 1
# 출력:

# 1 1
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
import sys
sys.setrecursionlimit(10**8)
n, m=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
answer=-1
time=0
t=0
def dfs(y, x):
    for i in range(4):
        ny, nx=y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<m and graph[ny][nx]>0 and not visited[ny][nx]:
            visited[ny][nx]=True
            dfs(ny, nx)
while graph!=[[0 for _ in range(m)] for _ in range(n)]:
    cnt=0
    t+=1
    visited=[[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                continue
            else:
                graph[i][j]-=1
    for i in range(n):
        for j in range(m):
            if graph[i][j]>0 and not visited[i][j]:
                cnt+=1
                dfs(i, j)
    if cnt>answer:
        time=t
        answer=cnt
print(time, answer)
