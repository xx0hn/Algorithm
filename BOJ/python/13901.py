# 문제
# 해빈이는 로봇을 좋아한다. 로봇을 가지고 놀던 해빈이는 로봇에게 계속해서 명령을 내려 움직이는 대신 이동할 방향을 미리 지정하여 로봇이 알아서 움직이도록 하였다.  이 로봇은 다음과 같은 규칙을 가지고 움직인다.
#
# 로봇은 사용자가 지정한 방향을 일직선으로 움직인다.
# 이동 중 벽이나 방문한 지역, 장애물을 만날 경우 로봇은 사용자가 지정한 다음 방향으로 움직인다.
# 사용자가 지정한 다음 방향이 없다면 맨 처음 방향으로 돌아가서 위의 과정을 반복한다.
# 로봇이 움직일 수 없을 경우 동작을 멈춘다.
# * * *
#
# x 0 *
#
# * * *
#
# <초기 상태>
#
# * 1 *
#
# x 0 *
#
# * * *
#
# <1번 째 이동>
#
# 2 1 *
#
# x 0 *
#
# * * *
#
# <2번 째 이동>
#
# 방 크기가 3* 3이고
#
# 장애물이 (1, 0)에 있으며
#
# 시작 위치는 (1,1)
#
# 해빈이가 지정한 방향이 (상, 하, 좌, 우) 일 때,
#
# 로봇의 마지막 위치는 (0, 0)이다.
#
# 2 번째 이동이 끝난 후, 로봇은 움직일 수 없으므로 동작을 멈춘다.
#
# 로봇은 (1, 1) → (0, 1) → (0, 0)로 이동하였다.
#
# 입력으로 방의 크기와 장애물의 개수, 각 장애물들의 위치, 로봇의 시작 위치, 이동 방향의 순서가 주어졌을 때 로봇이 멈추는 위치를 출력하시오. 위치 (0, 0)은 왼쪽 위를 가리키며 방의 크기가 R * C일 때 오른쪽 아래 위치는 (R - 1, C - 1)이 된다. (R은 세로의 크기를 C은 가로의 크기를 말한다.)
#
# 입력
# 첫 번째 줄에는 방의 크기 R, C(3 ≤ R, C ≤ 1,000)가 입력된다. 두 번째 줄에는 장애물의 개수 k(0 ≤ k ≤ 1,000)가 입력된다. 다음 k개의 줄에는 각 장애물 위치 br(0 ≤ br ≤ R – 1), bc(0 ≤ bc ≤ C - 1)가 주어진다. 그 다음 순서대로 로봇의 시작 위치 sr(0 ≤ sr ≤ R – 1), sc(0 ≤ sc ≤ C - 1)와 이동 방향의 순서(총 4개가 입력되는데 1은 위 방향, 2은 아래 방향, 3은 왼쪽 방향, 4는 오른쪽 방향을 나타낸다)가 한 줄씩 입력된다. 로봇의 시작위치에 장애물이 있는 경우는 없다.
#
# 출력
# 로봇의 마지막 위치 r, c를 출력한다.
r, c = map(int, input().split())
k = int(input())
grid = [['*' for _ in range(c)] for _ in range(r)]
for _ in range(k):
    a, b = map(int, input().split())
    grid[a][b] = 'x'
robot = list(map(int, input().split()))
grid[robot[0]][robot[1]] = '0'
commands = list(map(int, input().split()))
for i in range(len(commands)):
    commands[i] -= 1
dy, dx=[-1, 1, 0, 0], [0, 0, -1, 1]
def move(d):
    global robot
    while True:
        ny, nx = robot[0] + dy[d], robot[1] + dx[d]
        if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == '*':
            robot = [ny, nx]
            grid[ny][nx] = '0'
        else:
            break
idx = 0
while True:
    move(commands[idx])
    idx = (idx + 1) % 4
    cnt = 0
    for i in range(4):
        ny, nx = robot[0] + dy[i], robot[1] + dx[i]
        if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] == '*':
            cnt += 1
    if not cnt:
        break
print(*robot)
