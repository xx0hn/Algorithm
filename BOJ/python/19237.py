# 문제
# 청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.
#
# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.
#
# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
#
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
#
#
#
# <그림 1>
#
# 우선 순위
# 상어 1	상어 2	상어 3	상어 4
# ↑	↓ ← ↑ →	↑	↓ → ← ↑	↑	→ ← ↓ ↑	↑	← → ↑ ↓
# ↓	→ ↑ ↓ ←	↓	↓ ↑ ← →	↓	↑ → ← ↓	↓	← ↓ → ↑
# ←	← → ↓ ↑	←	← → ↑ ↓	←	↑ ← ↓ →	←	↑ → ↓ ←
# →	→ ← ↑ ↓	→	→ ↑ ↓ ←	→	← ↓ ↑ →	→	↑ → ↓ ←
# <표 1>
#
# <그림 1>은 맨 처음에 모든 상어가 자신의 냄새를 뿌린 상태를 나타내며, <표 1>에는 각 상어 및 현재 방향에 따른 우선순위가 표시되어 있다. 이 예제에서는 k = 4이다. 왼쪽 하단에 적힌 정수는 냄새를 의미하고, 그 값은 사라지기까지 남은 시간이다. 좌측 상단에 적힌 정수는 상어의 번호 또는 냄새를 뿌린 상어의 번호를 의미한다.
#
#
#
# <그림 2>
#
#
#
# <그림 3>
#
# <그림 2>는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태이고, <그림 3>은 <그림 2>의 상태에서 한 칸 더 이동한 것이다. (2, 4)에는 상어 2과 4가 같이 도달했기 때문에, 상어 4는 격자 밖으로 쫓겨났다.
#
#
#
# <그림 4>
#
#
#
# <그림 5>
#
# <그림 4>은 격자에 남아있는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태, <그림 5>는 <그림 4>에서 한 칸 더 이동한 상태를 나타낸다. 상어 2는 인접한 칸 중에 아무 냄새도 없는 칸이 없으므로 자신의 냄새가 들어있는 (2, 4)으로 이동했다. 상어가 이동한 후에, 맨 처음에 각 상어가 뿌린 냄새는 사라졌다.
#
# 이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)
#
# 그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.
#
# 그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
#
# 그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 두 번째 줄은 아래를 향할 때의 우선순위, 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.
#
# 맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.
#
# 출력
# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
from collections import deque
n, m, k=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
d=list(map(int, input().split()))
for i in range(m):
    d[i]-=1
priority=[[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))
        for j in range(4):
            priority[i][-1][j]-=1
shark=deque()
smell=[[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]!=0:
            smell[i][j]=[grid[i][j], k]
            shark.append((grid[i][j], i, j))
dy, dx=[-1, 1, 0, 0], [0, 0, -1, 1]
def move():
    tmp=[[0 for _ in range(n)] for _ in range(n)]
    new_shark=deque()
    while shark:
        num, y, x=shark.popleft()
        chk=False
        for nd in priority[num-1][d[num-1]]:
            ny, nx=y+dy[nd], x+dx[nd]
            if 0<=ny<n and 0<=nx<n:
                if not smell[ny][nx]:
                    new_shark.append((num, ny, nx))
                    d[num-1]=nd
                    chk=True
                    break
        if not chk:
            for nd in priority[num-1][d[num-1]]:
                ny, nx=y+dy[nd], x+dx[nd]
                if 0<=ny<n and 0<=nx<n:
                    if smell[ny][nx] and smell[ny][nx][0]==num:
                        new_shark.append((num, ny, nx))
                        d[num-1]=nd
                        break
    for sn, y, x in new_shark:
        if tmp[y][x]==0:
            tmp[y][x]=sn
        else:
            if tmp[y][x]>sn:
                tmp[y][x]=sn
    for i in range(n):
        for j in range(n):
            grid[i][j]=tmp[i][j]
            if tmp[i][j]!=0:
                shark.append((tmp[i][j], i, j))
                smell[i][j]=[tmp[i][j], k]
def decrease_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                if smell[i][j][1]==0:
                    smell[i][j]=[]
                else:
                    smell[i][j][1]-=1
def check_shark():
    if len(shark)==1:
        return True
    return False
answer=0
while not check_shark():
    if answer>=1000:
        answer=-1
        break
    answer+=1
    decrease_smell()
    move()
print(answer)
