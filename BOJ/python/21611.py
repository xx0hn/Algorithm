# 문제
# 마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그, 비바라기 마법을 할 수 있다. 오늘 새로 배운 마법은 블리자드이고, 크기가 N×N인 격자에서 연습하려고 한다. N은 항상 홀수이고, (r, c)는 격자의 r행 c열을 의미한다. 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이며 마법사 상어는 ((N+1)/2, (N+1)/2)에 있다.
#
# 일부 칸과 칸 사이에는 벽이 세워져 있으며, 다음은 N = 3, 5, 7인 경우의 예시이다. 실선은 벽이고, 점선은 벽이 아니다. 칸에 적혀있는 수는 칸의 번호이다.
#
# 가장 처음에 상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다. 구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다. 같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬이라고 한다. 다음은 N = 7인 경우 예시이다.
#
# 블리자드 마법을 시전하려면 방향 di와 거리 si를 정해야 한다. 총 4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4로 나타낸다. 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다. 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다. 얼음 파편은 벽의 위로 떨어지기 때문에, 벽은 파괴되지 않는다.
#
# 다음 예시는 방향은 아래, 거리는 2인 경우이다.
#
# 만약 어떤 칸 A의 번호보다 번호가 하나 작은 칸이 빈 칸이면, A에 있는 구슬은 그 빈 칸으로 이동한다. 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복된다. 따라서, 구슬이 파괴된 후에는 빈 칸이 생겨 구슬이 이동하고, 구슬이 모두 이동한 결과는 다음과 같다.
#
# 이제 구슬이 폭발하는 단계이다. 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다. 다음은 왼쪽 그림은 위의 상태에서 폭발하는 구슬이 들어있는 칸을 파란색과 초록색으로 표시한 것이고, 오른쪽 그림은 구슬이 폭발한 후의 상태이다.
#
# 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다. 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계이고, 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복된다. 구슬이 폭발한 후의 상태에서 구슬이 이동하면 다음과 같다.
#
# 위의 상태는 4개 이상 연속하는 구슬이 있기 때문에 구슬이 다시 폭발하게 된다.
#
# 이제 더 이상 폭발한 구슬이 없기 때문에, 구슬이 변화하는 단계가 된다. 연속하는 구슬은 하나의 그룹이라고 한다. 다음은 1번 구슬은 빨간색, 2번 구슬은 파란색, 3번 구슬은 보라색으로 표시한 그림이다.
#
# 하나의 그룹은 두 개의 구슬 A와 B로 변한다. 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호이다. 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다. 다음 그림은 구슬이 변화한 후이고, 색은 구분하기 위해 위의 그림에 있는 그룹의 색을 그대로 사용했다. 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
#
# 마법사 상어는 블리자드를 총 M번 시전했다. 시전한 마법의 정보가 주어졌을 때, 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)를 구해보자.
#
# 입력
# 첫째 줄에 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 격자에 들어있는 구슬의 정보가 주어진다. r번째 행의 c번째 정수는 (r, c)에 들어있는 구슬의 번호를 의미한다. 어떤 칸에 구슬이 없으면 0이 주어진다. 상어가 있는 칸도 항상 0이 주어진다.
#
# 다음 M개의 줄에는 블리자드 마법의 방향 di와 거리 si가 한 줄에 하나씩 마법을 시전한 순서대로 주어진다.
#
# 출력
# 첫째 줄에 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)를 출력한다.
#
# 제한
# 3 ≤ N ≤ 49
# N은 홀수
# 1 ≤ M ≤ 100
# 1 ≤ di ≤ 4
# 1 ≤ si ≤ (N-1)/2
# 칸에 들어있는 구슬이 K개라면, 구슬이 들어있는 칸의 번호는 1번부터 K번까지이다.
# 입력으로 주어진 격자에는 4개 이상 연속하는 구슬이 없다.
import copy
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = []
for _ in range(m):
    di, si = map(int, input().split())
    commands.append((di-1, si))
nums = [[0 for _ in range(n)] for _ in range(n)]
idxs = []
center = (n//2, n//2)
marbles = [0, 0, 0, 0]
ndy, ndx = [0, 1, 0, -1], [1, 0, -1, 0]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def get_nums():
    q = deque()
    q.append((0, 0, n*n-1))
    nums[0][0] = n*n-1
    d = 0
    while q:
        y, x, num = q.popleft()
        idxs.append((y, x))
        if (y, x) == center:
            break
        ny, nx = y+ndy[d], x+ndx[d]
        if 0 <= ny < n and 0 <= nx < n and not nums[ny][nx]:
            nums[ny][nx] = num-1
            q.append((ny, nx, num-1))
        else:
            d = (d+1)%4
            ny, nx = y+ndy[d], x+ndx[d]
            nums[ny][nx] = num-1
            q.append((ny, nx, num-1))
def destroy(command):
    d, s = command
    y, x = center
    for i in range(1, s+1):
        ny, nx = y+(dy[d]*i), x+(dx[d]*i)
        if 0 <= ny < n and 0 <= nx < n:
            grid[ny][nx] = 0
def move():
    for i in range(1, len(idxs)-1):
        if not grid[idxs[i][0]][idxs[i][1]]:
            cur = i
            for j in range(i+1, len(idxs)):
                if grid[idxs[j][0]][idxs[j][1]]:
                    grid[idxs[cur][0]][idxs[cur][1]], grid[idxs[j][0]][idxs[j][1]] = grid[idxs[j][0]][idxs[j][1]], 0
                    cur += 1
            break
def explode():
    i = 1
    while i < len(idxs)-1:
        if grid[idxs[i][0]][idxs[i][1]]:
            std = grid[idxs[i][0]][idxs[i][1]]
            cnt = [(idxs[i][0], idxs[i][1])]
            for j in range(i+1, len(idxs)):
                if grid[idxs[j][0]][idxs[j][1]] == std:
                    cnt.append((idxs[j][0], idxs[j][1]))
                else:
                    break
            if len(cnt) >= 4:
                for y, x in cnt:
                    marbles[grid[y][x]] += 1
                    grid[y][x] = 0
            i += len(cnt)
        else:
            break
def to_ab():
    global grid
    groups = []
    tmp = grid[idxs[1][0]][idxs[1][1]]
    cnt = 0
    for y, x in idxs[1:]:
        if grid[y][x] == tmp:
            cnt += 1
            tmp = grid[y][x]
        else:
            groups.append((cnt, tmp))
            cnt = 1
            tmp = grid[y][x]
    cur = 1
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in groups:
        if cur > len(idxs)-1:
            break
        grid[idxs[cur][0]][idxs[cur][1]] = a
        cur += 1
        if cur > len(idxs)-1:
            break
        grid[idxs[cur][0]][idxs[cur][1]] = b
        cur += 1
get_nums()
idxs = idxs[::-1]
for i in range(m):
    destroy(commands[i])
    move()
    while True:
        tmp = copy.deepcopy(grid)
        explode()
        move()
        if tmp == grid:
            break
    to_ab()
answer = 0
for i in range(1, 4):
    answer += marbles[i]*i
print(answer)
