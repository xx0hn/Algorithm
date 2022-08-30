# 문제
# 평화롭게 문제를 경작하며 생활하는 BOJ 마을 사람들은 더 이상 2차원 미로에 흥미를 느끼지 않는다. 2차원 미로는 너무나 쉽게 탈출이 가능하기 때문이다. 미로를 이 세상 그 누구보다 사랑하는 준현이는 이런 상황을 매우 안타깝게 여겨 아주 큰 상금을 걸고 BOJ 마을 사람들의 관심을 확 끌 수 있는 3차원 미로 탈출 대회를 개최하기로 했다.
#
# 대회의 규칙은 아래와 같다.
#
# 5×5 크기의 판이 5개 주어진다. 이중 일부 칸은 참가자가 들어갈 수 있고 일부 칸은 참가자가 들어갈 수 없다. 그림에서 하얀 칸은 참가자가 들어갈 수 있는 칸을, 검은 칸은 참가자가 들어갈 수 없는 칸을 의미한다.
#
#
# 참가자는 주어진 판들을 시계 방향, 혹은 반시계 방향으로 자유롭게 회전할 수 있다. 그러나 판을 뒤집을 수는 없다.
#
#
# 회전을 완료한 후 참가자는 판 5개를 쌓는다. 판을 쌓는 순서는 참가자가 자유롭게 정할 수 있다. 이렇게 판 5개를 쌓아 만들어진 5×5×5 크기의 큐브가 바로 참가자를 위한 미로이다. 이 때 큐브의 입구는 정육면체에서 참가자가 임의로 선택한 꼭짓점에 위치한 칸이고 출구는 입구와 면을 공유하지 않는 꼭짓점에 위치한 칸이다.
#
#
# 참가자는 현재 위치한 칸에서 면으로 인접한 칸이 참가자가 들어갈 수 있는 칸인 경우 그 칸으로 이동할 수 있다.
# 참가자 중에서 본인이 설계한 미로를 가장 적은 이동 횟수로 탈출한 사람이 우승한다. 만약 미로의 입구 혹은 출구가 막혀있거나, 입구에서 출구에 도달할 수 있는 방법이 존재하지 않을 경우에는 탈출이 불가능한 것으로 간주한다.
# 이 대회에서 우승하기 위해서는 미로를 잘 빠져나올 수 있기 위한 담력 증진과 체력 훈련, 그리고 적절한 운이 제일 중요하지만, 가장 적은 이동 횟수로 출구에 도달할 수 있게끔 미로를 만드는 능력 또한 없어서는 안 된다. 주어진 판에서 가장 적은 이동 횟수로 출구에 도달할 수 있게끔 미로를 만들었을 때 몇 번 이동을 해야하는지 구해보자.
#
# 입력
# 첫째 줄부터 25줄에 걸쳐 판이 주어진다. 각 판은 5줄에 걸쳐 주어지며 각 줄에는 5개의 숫자가 빈칸을 사이에 두고 주어진다. 0은 참가자가 들어갈 수 없는 칸, 1은 참가자가 들어갈 수 있는 칸을 의미한다.
#
# 출력
# 첫째 줄에 주어진 판으로 설계된 미로를 탈출하는 가장 적은 이동 횟수를 출력한다. 단, 어떻게 설계하더라도 탈출이 불가능할 경우에는 -1을 출력한다.
from itertools import permutations
from collections import deque
grid = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
tmp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
dz, dy, dx = [0, 0, 1, 0, -1, 0], [0, 0, 0, 1, 0, -1], [1, -1, 0, 0, 0, 0]
answer = 1e9
def rotate_grid(lst):
    rotated = list(zip(*lst[::-1]))
    for i in range(5):
        rotated[i] = list(rotated[i])
    return rotated
def move(grid):
    global answer
    q = deque()
    q.append((0, 0, 0, 0))
    visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    while q:
        z, y, x, cnt = q.popleft()
        if (z, y, x) == (4, 4, 4):
            if cnt == 12:
                print(cnt)
                quit()
            answer = min(answer, cnt)
            return
        for i in range(6):
            nz, ny, nx = z+dz[i], y+dy[i], x+dx[i]
            if 0 <= nz < 5 and 0 <= ny < 5 and 0 <= nx < 5:
                if grid[nz][ny][nx] == 1 and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    q.append((nz, ny, nx, cnt+1))
def dfs(cur):
    if cur == 5:
        if tmp[4][4][4]:
            move(tmp)
        return
    for i in range(4):
        if tmp[0][0][0]:
            dfs(cur+1)
        tmp[cur] = rotate_grid(tmp[cur])
for i in permutations([0, 1, 2, 3, 4]):
    for j in range(5):
        tmp[i[j]] = grid[j]
    dfs(0)
if answer == 1e9:
    answer = -1
print(answer)
