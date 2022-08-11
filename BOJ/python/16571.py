# 문제
# 틱택토(Tic-tac-toe) 게임은 두 플레이어가 번갈아가며 O와 X를 3x3판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하는 게임이다.
#
# 먼저 3개의 연속 된 O 또는 X를 완성시킨 플레이어가 승리하게 된다. 이 게임은 무승부가 가능하다.
#
#
#
# Figure: 게임의 진행과정 예시
#
# 틱택토 초보 승현이와 기영이는 틱택토 게임을 플레이하고 있었다. 그런데 뒤에서 지켜보고 있던 틱택토 초고수 윤영이와 진욱이가 너무나 답답한 나머지 본인들이 대신 플레이를 해주겠다고 나섰다.
#
# 지금까지 진행 된 틱택토 게임 보드가 주어졌을 때, 이번에 착수하는 플레이어가 얻을 수 있는 최선의 게임 결과는 무엇일까? 단, 두 플레이어는 항상 모든 경우를 고려하여 최선의 수를 둔다고 가정한다.
#
# 입력
# 현재까지 진행된 틱택토 게임 보드가 띄어쓰기로 구분되어 3줄에 걸쳐 주어진다. 0은 빈칸, 1은 X, 2는 O를 의미한다. 단, 항상 X가 선공이다. 그리고 이미 게임이 종료된 상태는 입력으로 주어지지 않는다.
#
# 출력
# 첫째 줄에 주어진 게임 보드에서 이번에 착수하는 플레이어가 얻을 수 있는 최선의 게임 결과를 출력한다.
#
# 이기는 경우 "W", 무승부인 경우 "D", 지는 경우 "L"을 출력한다.
grid = [list(map(int, input().split())) for _ in range(3)]
x, o = 0, 0
blanks = []
me = 0
for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            x += 1
        if grid[i][j] == 2:
            o += 1
        if grid[i][j] == 0:
            blanks.append((i, j))
if x == o:
    me = 1
else:
    me = 2
def chk(turn):
    if turn == 1:
        before = 2
    else:
        before = 1
    if (grid[0][0] == grid[1][1] == grid[2][2] == before) or (grid[0][2] == grid[1][1] == grid[2][0] == before):
        return True
    for i in range(3):
        if (grid[i][0] == grid[i][1] == grid[i][2] == before) or (grid[0][i] == grid[1][i] == grid[2][i] == before):
            return True
    return False
def tic_tac_toe(cur):
    if cur == 1:
        nxt = 2
    else:
        nxt = 1
    mn = 2
    if chk(cur):
        return -1
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                grid[i][j] = cur
                mn = min(mn, tic_tac_toe(nxt))
                grid[i][j] = 0
    if mn == 1:
        return -1
    elif mn == 2 or mn == 0:
        return 0
    else:
        return 1
if not blanks:
    print('D')
else:
    answer = tic_tac_toe(me)
    if answer == 1:
        print('W')
    elif answer == 0:
        print('D')
    else:
        print('L')
