# 문제
# 마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그, 비바라기, 블리자드 마법을 할 수 있다. 오늘은 기존에 배운 물복사버그 마법의 상위 마법인 복제를 배웠고, 4 × 4 크기의 격자에서 연습하려고 한다. (r, c)는 격자의 r행 c열을 의미한다. 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (4, 4)이다.
#
# 격자에는 물고기 M마리가 있다. 각 물고기는 격자의 칸 하나에 들어가 있으며, 이동 방향을 가지고 있다. 이동 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다. 마법사 상어도 연습을 위해 격자에 들어가있다. 상어도 격자의 한 칸에 들어가있다. 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.
#
# 상어의 마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.
#
# 상어가 모든 물고기에게 복제 마법을 시전한다. 복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
# 모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다. 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기의 냄새는 아래 3에서 설명한다.
# 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다. 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.
# 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
# 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
# 격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 그리고 연습 횟수 S가 주어진다. S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
#
# 입력
# 첫째 줄에 물고기의 수 M, 상어가 마법을 연습한 횟수 S가 주어진다. 둘째 줄부터 M개의 줄에는 물고기의 정보 fx, fy, d가 주어진다. (fx, fy)는 물고기의 위치를 의미하고, d는 방향을 의미한다. 방향은 8 이하의 자연수로 표현하고, 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 마지막 줄에는 sx, sy가 주어지며, 상어가 (sx, sy)에 있음을 의미한다.
#
# 격자 위에 있는 물고기의 수가 항상 1,000,000 이하인 입력만 주어진다.
#
# 출력
# S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력한다.
#
# 제한
# 1 ≤ M ≤ 10
# 1 ≤ S ≤ 100
# 1 ≤ fx, fy, sx, sy ≤ 4
# 1 ≤ d ≤ 8
# 두 물고기 또는 물고기와 상어가 같은 칸에 있을 수도 있다.
import copy

m, s = map(int, input().split())
grid = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    fy, fx, d = map(int, input().split())
    grid[fy-1][fx-1].append(d-1)
dy, dx = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
sdy, sdx = [-1, 0, 1, 0], [0, -1, 0, 1]
sy, sx = map(int, input().split())
shark = [sy-1, sx-1]
smell = [[0 for _ in range(4)] for _ in range(4)]
shark_move = []
def move_shark(y, x, cur, cnt, move):
    global max_eaten, shark, eaten
    if cur == 3:
        if max_eaten < cnt:
            max_eaten = cnt
            shark = [y, x]
            eaten = move[:]
        return
    for i in range(4):
        ny, nx = y+sdy[i], x+sdx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if (ny, nx) not in set(move):
                move_shark(ny, nx, cur+1, cnt+len(tmp_grid[ny][nx]), move+[(ny, nx)])
            else:
                move_shark(ny, nx, cur+1, cnt, move)
def move_fish():
    global tmp_grid
    result = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while tmp_grid[i][j]:
                nd = tmp_grid[i][j].pop()
                for l in range(nd, nd-8, -1):
                    l %= 8
                    ny, nx = i+dy[l], j+dx[l]
                    if (ny, nx) != tuple(shark) and 0 <= ny < 4 and 0 <= nx < 4 and not smell[ny][nx]:
                        result[ny][nx].append(l)
                        break
                else:
                    result[i][j].append(nd)
    tmp_grid = copy.deepcopy(result)
def copy_complete():
    for i in range(4):
        for j in range(4):
            if tmp_grid[i][j]:
                grid[i][j] += tmp_grid[i][j]
def decrease_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
for _ in range(s):
    eaten = []
    max_eaten = -1
    tmp_grid = copy.deepcopy(grid)
    move_fish()
    move_shark(shark[0], shark[1], 0, 0, [])
    for y, x in eaten:
        if tmp_grid[y][x]:
            tmp_grid[y][x] = []
            smell[y][x] = 3
    decrease_smell()
    copy_complete()
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(grid[i][j])
print(answer)
