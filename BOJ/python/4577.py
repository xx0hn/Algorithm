# 문제
# 소코반은 1982년에 일본에서 만들어진 게임으로, 일본어로 창고지기라는 뜻이다. 이 게임은 캐릭터를 이용해 창고 안에 있는 박스를 모두 목표점으로 옮기는 게임이다. 목표점의 수와 박스의 수는 같다. 플레이어는 화살표(위, 아래, 왼쪽, 오른쪽)를 이용해 캐릭터를 아래와 같은 규칙으로 조정할 수 있다.
#
# 캐릭터에게 지시한 방향이 빈 칸(박스나 벽이 아닌 곳)인 경우에는 그 칸으로 이동한다.
# 지시한 방향에 박스가 있는 경우에는, 박스를 민다. 이 경우에는 박스가 이동할 칸도 비어있어야 한다.
# 지시한 방향이 벽인 경우, 또는 박스가 있는데, 박스가 이동할 칸에 다른 박스나 벽이 있는 경우에는 키를 눌러도 캐릭터는 이동하지 않는다.
# 모든 박스를 목표점으로 이동시킨 경우에 게임은 끝난다. 게임이 끝난 후에 입력하는 키는 모두 무시된다.
#
# 준규는 소코반으로 고통받는 친구들을 위해서 소코반의 해를 찾는 프로그램을 작성하려고 한다. 하지만, 소코반의 해를 찾는 문제는 NP-hard와 PSPACE-complete에 속하고, 매우 어려운 문제이다. 따라서, 간단한 소코반 프로그램을 작성해보려고 한다.
#
# 사용자가 입력한 키가 순서대로 주어졌을 때, 게임이 어떻게 진행되는지를 구하는 프로그램을 작성하시오.
#
# 게임의 상태는 아래와 같은 문자로 나타낼 수 있다.
#
# 문자	뜻
# .	빈 공간
# #	벽
# +	비어 있는 목표점
# b	박스
# B	목표점 위에 있는 박스
# w	캐릭터
# W	목표점 위에 있는 캐릭터
# 첫 번째 입력은 문제의 그림과 같다.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스의 첫째 줄에는 행과 열의 수 R, C가 주어진다. (4 ≤ R ≤ 15, 4 ≤ C ≤ 15) 다음 R개 줄에는 현재 게임의 상태가 주어진다. 모든 줄은 C개의 문자로 이루어져 있다. 마지막 줄에는 플레이어가 입력한 키가 순서대로 주어지며 길이는 최대 50이다. 위, 아래, 왼쪽, 오른쪽은 U, D, L, R로 나타낸다.
#
# 입력의 마지막 줄에는 0 0이 주어진다.
#
# 입력으로 주어지는 모든 데이터는 항상 캐릭터가 한 명이고, 박스의 수와 목표점의 수는 같다. 또, 목표점 위에 올라가 있지 않은 박스는 적어도 한 개 이며, 가장 바깥쪽 칸은 항상 벽이다.
#
# 출력
# 각각의 게임에 대해서, 게임 번호를 출력한 다음에 게임이 끝났으면 complete를, 아니면 incomplete를 출력한다. 그 다음 줄부터 R개 줄에는 게임의 상태를 출력한다.
def move(command):
    global cur
    d = mapping[command]
    y, x = cur
    ny, nx = y+dy[d], x+dx[d]
    if 0 <= ny < r and 0 <= nx < c and grid[ny][nx] != '#':
        if grid[ny][nx] == 'b' or grid[ny][nx] == 'B':
            nxt_y, nxt_x = ny+dy[d], nx+dx[d]
            if 0 <= nxt_y < r and 0 <= nxt_x < c and grid[nxt_y][nxt_x] not in ('#', 'b', 'B'):
                cur = [ny, nx]
                grid[ny][nx], grid[nxt_y][nxt_x] = '.', 'b'
        else:
            cur = [ny, nx]
def grid_setting():
    grid[cur[0]][cur[1]] = 'w'
    for y, x in point:
        if grid[y][x].isalpha():
            grid[y][x] = grid[y][x].upper()
        else:
            grid[y][x] = '+'
def chk_complete():
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'b':
                return False
    return True
idx = 1
while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    grid = [list(str(input())) for _ in range(r)]
    commands = list(str(input()))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    mapping = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    cur = []
    point = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] in ('+', 'W', 'B'):
                point.append((i, j))
            if grid[i][j] == 'w':
                cur = [i, j]
                grid[i][j] = '.'
            if grid[i][j] == 'W':
                cur = [i, j]
                grid[i][j] = '+'
    flag = False
    for command in commands:
        if chk_complete():
            grid_setting()
            print("Game " + str(idx) + ": " + "complete")
            for i in range(r):
                print(''.join(grid[i]))
            flag = True
            break
        grid[cur[0]][cur[1]] = '.'
        move(command)
        grid_setting()
    if not flag:
        if chk_complete():
            print("Game "+str(idx)+": "+"complete")
        else:
            print("Game "+str(idx)+": "+"incomplete")
        for i in range(r):
            print(''.join(grid[i]))
    idx += 1
