# 문제
# 가로와 세로의 길이가 같은 평지에서 벌목을 한다. 그 지형은 0과 1로 나타나 있다. 1은 아직 잘려지지 않은 나무를 나타내고 0은 아무 것도 없음을 나타낸다. 다음 지형을 보자.
#
# B 0 0 1 1
# B 0 0 0 0
# B 0 0 0 0
# 1 1 0 0 0
# E E E 0 0
# 위의 지형에서 길이 3인 통나무 BBB를 밀거나 회전시켜 EEE의 위치로 옮기는 작업을 하는 문제를 생각해 보자. BBB와 EEE의 위치는 임의로 주어진다. 단 문제에서 통나무의 길이는 항상 3이며 B의 개수와 E의 개수는 같다. 통나무를 움직이는 방법은 아래와 같이 상하좌우(Up, Down, Left, Right)와 회전(Turn)이 있다.
#
# 코드	의미
# U	통나무를 위로 한 칸 옮긴다.
# D	통나무를 아래로 한 칸 옮긴다.
# L	통나무를 왼쪽으로 한 칸 옮긴다.
# R	통나무를 오른쪽으로 한 칸 옮긴다.
# T	중심점을 중심으로 90도 회전시킨다.
# 예를 들면, 다음과 같다. (초기상태로부터의 이동)
#
# 초기상태	상(U)	하(D)	좌(L)	우(R)	회전(T)
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 B B B 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 B B B 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 B B B 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# B B B 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 B B B 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 B 0 0 0
# 0 0 B 0 0 0
# 0 0 B 0 0 0
# 0 0 0 1 0 0
# 이와 같은 방식으로 이동시킬 때에 그 움직일 위치에 다른 나무, 즉 1이 없어야만 움직일 수 있다. 그리고 움직임은 위의 그림과 같이 한 번에 한 칸씩만 움직인다. 단 움직이는 통나무는 어떤 경우이든지 중간단계에서 한 행이나 한 열에만 놓일 수 있다. 예를 들면 아래 그림에서 a와 같은 단계는 불가능하다. 그리고 회전의 경우에서는 반드시 중심점을 중심으로 90도 회전을 해야 한다. (항상 통나무의 길이가 3이므로 중심점이 있음)
#
# 그리고 이런 회전(Turn)이 가능하기 위해서는 그 통나무를 둘러싸고 있는 3*3 정사각형의 구역에 단 한 그루의 나무도 없어야만 한다. 즉, 아래그림 b, d와 같이 ?로 표시된 지역에 다른 나무, 즉 1이 없어야만 회전시킬 수 있다. 따라서 c와 같은 경우에, 통나무는 왼쪽 아직 벌채되지 않은 나무 때문에 회전시킬 수 없다.
#
# a	b	c	d
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 B 0 0
# 0 0 B 0 0 0
# 0 B 0 0 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 ? ? ? 0
# 0 0 B B B 0
# 0 0 ? ? ? 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 1 B 0 0
# 0 0 0 B 0 0
# 0 0 0 B 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 ? B ? 0
# 0 0 ? B ? 0
# 0 0 ? B ? 0
# 0 0 0 0 0 0
# 문제는 통나무를 5개의 기본동작(U, D, L, R, T)만을 사용하여 처음위치(BBB)에서 최종위치(EEE)로 옮기는 프로그램을 작성하는 것이다. 단, 최소 횟수의 단위 동작을 사용해야 한다.
#
# 입력
# 첫째 줄에 주어진 평지의 한 변의 길이 N이 주어진다. (4 ≤ N ≤ 50) 주어진다. 이어서 그 지형의 정보가 0, 1, B, E로 이루어진 문자열로 주어진다. 한 줄에 입력되는 문자열의 길이는 N이며 입력 문자 사이에는 빈칸이 없다. 통나무와 최종 위치의 개수는 1개이다.
#
# 출력
# 첫째 줄에 최소 동작 횟수를 출력한다. 이동이 불가능하면 0만을 출력한다.
from collections import deque
n = int(input())
grid = [list(str(input())) for _ in range(n)]
tree = []
dest = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'B':
            tree.append((i, j))
            grid[i][j] = '0'
        if grid[i][j] == 'E':
            dest.append((i, j))
if tree[0][0] == tree[1][0] == tree[2][0]: # 가로 모양
    tree = [tree[1], 0]
else: # 세로 모양
    tree = [tree[1], 1]
if dest[0][0] == dest[1][0] == dest[2][0]:
    dest = [dest[1], 0]
else:
    dest = [dest[1], 1]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def chk_square(y, x):
    sdy, sdx = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(8):
        ny, nx = y+sdy[i], x+sdx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if grid[ny][nx] == '1':
                return False
        else:
            return False
    return True
def chk_nxt_tree(y, x, type):
    if type == 0:
        if 0 <= y < n and 0 <= x-1 < n and 0 <= x < n and 0 <= x+1 < n and grid[y][x] != '1' and grid[y][x-1] != '1' and grid[y][x+1] != '1':
            return True
        return False
    elif type == 1:
        if 0 <= y-1 < n and 0 <= y < n and 0 <= y+1 < n and 0 <= x < n and grid[y-1][x] != '1' and grid[y][x] != '1' and grid[y+1][x] != '1':
            return True
        return False
def bfs():
    q = deque()
    q.append((tree[0][0], tree[0][1], tree[1], 0))
    visited = [[[False for _ in range(2)] for _ in range(n)] for _ in range(n)]
    visited[tree[0][0]][tree[0][1]][tree[1]] = True
    while q:
        y, x, type, time = q.popleft()
        if [(y, x), type] == dest:
            return time
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if chk_nxt_tree(ny, nx, type) and not visited[ny][nx][type]:
                visited[ny][nx][type] = True
                q.append((ny, nx, type, time+1))
        if chk_square(y, x) and not visited[y][x][1-type]:
            visited[y][x][1-type] = True
            q.append((y, x, 1-type, time+1))
    return 0
print(bfs())
