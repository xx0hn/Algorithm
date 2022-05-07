# 문제
# 아기 상어가 성장해 청소년 상어가 되었다.
#
# 4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.
#
# 오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.
#
# 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
#
# 물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
#
#
#
# <그림 1>
#
# <그림 1>은 청소년 상어가 공간에 들어가기 전 초기 상태이다. 상어가 공간에 들어가면 (0, 0)에 있는 7번 물고기를 먹고, 상어의 방향은 ↘이 된다. <그림 2>는 상어가 들어간 직후의 상태를 나타낸다.
#
#
#
# <그림 2>
#
# 이제 물고기가 이동해야 한다. 1번 물고기의 방향은 ↗이다. ↗ 방향에는 칸이 있고, 15번 물고기가 들어있다. 물고기가 있는 칸으로 이동할 때는 그 칸에 있는 물고기와 위치를 서로 바꿔야 한다. 따라서, 1번 물고기가 이동을 마치면 <그림 3>과 같아진다.
#
#
#
# <그림 3>
#
# 2번 물고기의 방향은 ←인데, 그 방향에는 상어가 있으니 이동할 수 없다. 방향을 45도 반시계 회전을 하면 ↙가 되고, 이 칸에는 3번 물고기가 있다. 물고기가 있는 칸이니 서로 위치를 바꾸고, <그림 4>와 같아지게 된다.
#
#
#
# <그림 4>
#
# 3번 물고기의 방향은 ↑이고, 존재하지 않는 칸이다. 45도 반시계 회전을 한 방향 ↖도 존재하지 않으니, 다시 회전을 한다. ← 방향에는 상어가 있으니 또 회전을 해야 한다. ↙ 방향에는 2번 물고기가 있으니 서로의 위치를 교환하면 된다. 이런 식으로 모든 물고기가 이동하면 <그림 5>와 같아진다.
#
#
#
# <그림 5>
#
# 물고기가 모두 이동했으니 이제 상어가 이동할 순서이다. 상어의 방향은 ↘이고, 이동할 수 있는 칸은 12번 물고기가 있는 칸, 15번 물고기가 있는 칸, 8번 물고기가 있는 칸 중에 하나이다. 만약, 8번 물고기가 있는 칸으로 이동하면, <그림 6>과 같아지게 된다.
#
#
#
# <그림 6>
#
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
#
# 입력
# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다. 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
#
# 출력
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.
import copy

grid=[[] for _ in range(4)]
fish=[[] for _ in range(17)]
for i in range(4):
    tmp=list(map(int, input().split()))
    for j in range(4):
        grid[i].append([tmp[2*j], tmp[2*j+1]-1])
for i in range(4):
    for j in range(4):
        fish[grid[i][j][0]]=[i, j]
dy, dx=[-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
shark=[0, 0, grid[0][0][1]]
fat=grid[0][0][0]
fish[grid[0][0][0]]=None
grid[0][0]=[0, 0]
answer=0
def move_fish(grid, fish):
    for num in range(1, 17):
        if fish[num] is None:
            continue
        y, x=fish[num]
        d=grid[y][x][1]
        for k in range(8):
            nd=(d+k)%8
            ny, nx=y+dy[nd], x+dx[nd]
            if 0<=ny<4 and 0<=nx<4:
                if (ny, nx)==(shark[0], shark[1]):
                    continue
                grid[y][x][1]=nd
                fish[grid[ny][nx][0]], fish[num]=[y, x], [ny, nx]
                grid[y][x], grid[ny][nx]=grid[ny][nx], grid[y][x]
                break
def move_shark(y, x, d, fat, tmp_grid, tmp_fish):
    global answer, shark
    shark=[y, x, d]
    move_fish(tmp_grid, tmp_fish)
    chk=False
    for i in range(1, 4):
        ny, nx=y+dy[d]*i, x+dx[d]*i
        if 0<=ny<4 and 0<=nx<4:
            grid=copy.deepcopy(tmp_grid)
            fish=copy.deepcopy(tmp_fish)
            if grid[ny][nx]!=[0, 0]:
                num=grid[ny][nx][0]
                fish[num]=None
                tmp=grid[ny][nx]
                grid[ny][nx]=[0, 0]
                chk=True
                move_shark(ny, nx, tmp[1], fat+tmp[grid[ny][nx][0]], grid, fish)
    if not chk:
        answer=max(answer, fat)
        return
move_shark(0, 0, shark[2], fat, grid, fish)
print(answer)