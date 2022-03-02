# 문제
# 미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.
#
#
#
# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.
#
# 1초 동안 아래 적힌 일이 순서대로 일어난다.
#
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 다음은 확산의 예시이다.
#
#
#
# 왼쪽과 오른쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.
#
#
#
# 인접한 네 방향으로 모두 확산이 일어난다.
#
#
#
# 공기청정기가 있는 칸으로는 확산이 일어나지 않는다.
#
# 공기청정기의 바람은 다음과 같은 방향으로 순환한다.
#
#
#
# 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
#
# 입력
# 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
#
# 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
#
# 출력
# 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
def spread():
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if not(0<=nx<r and 0<=ny<c): continue
                    if board[x][y]<5:continue
                    if (nx, ny)==(cleaner[0], 0): continue
                    if (nx, ny)==(cleaner[1], 0): continue
                    cnt+=1
                    board2[nx][ny]+=board[x][y]//5
                board2[x][y]+=(board[x][y]-board[x][y]//5*cnt)
def cleaning():
    for i in range(cleaner[0]-2, -1, -1):
        board2[i+1][0] = board2[i][0]
    for i in range(1, c):
        board2[0][i-1] = board2[0][i]
    for i in range(1, cleaner[0]+1):
        board2[i-1][-1] = board2[i][-1]
    for i in range(c-2, 0, -1):
        board2[cleaner[0]][i+1] = board2[cleaner[0]][i]
    board2[cleaner[0]][1] = 0
    for i in range(cleaner[1]+2, r):
        board2[i-1][0] = board2[i][0]
    for i in range(1, c):
        board2[-1][i-1] = board2[-1][i]
    for i in range(r-2, cleaner[1]-1, -1):
        board2[i+1][-1] = board2[i][-1]
    for i in range(c-2, 0, -1):
        board2[cleaner[1]][i+1] = board2[cleaner[1]][i]
    board2[cleaner[1]][1] = 0
r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for i in range(r):
    if board[i][0] == -1:
        cleaner.append(i)
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
board2 = [[0]*c for _ in range(r)]
spread()
cleaning()
for time in range(t-1):
    board = board2.copy()
    board2 = [[0]*c for _ in range(r)]
    spread()
    cleaning()
answer = 0
for i in range(r):
    for j in range(c):
        if board2[i][j] > 0:
            answer+=board2[i][j]
print(answer)
