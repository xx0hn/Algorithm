# 문제
# 십자가는 가운데에 '*'가 있고, 상하좌우 방향으로 모두 같은 길이의 '*'가 있는 모양이다. 십자가의 크기는 가운데를 중심으로 상하좌우 방향으로 있는 '*'의 개수이다. 십자가의 크기는 0보다 크거나 같아야 한다.
#
# 아래 그림은 크기가 0, 1, 2, 3인 십자가이고, 빈 칸은 '.'이다.
#
#                   ...*...
#           ..*..   ...*...
#     .*.   ..*..   ...*...
# *   ***   *****   *******
#     .*.   ..*..   ...*...
#           ..*..   ...*...
#                   ...*...
# 십자가의 넓이는 포함된 '*'의 개수이다. 크기가 0, 1, 2, 3인 십자가의 넓이는 1, 5, 9, 13이다.
#
# 크기가 N×M이고, '.'과 '#'로 이루어진 격자판이 주어진다. 격자판에 두 개의 십자가를 겹치지 않게 놓으려고 한다. 십자가는 '#'가 있는 칸에만 놓을 수 있다. 놓인 십자가 넓이의 곱의 최댓값을 구해보자.
#
# 입력
# 첫째 줄에 격자판의 크기 N, M (2 ≤ N, M ≤ 15)이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 상태가 주어진다. 항상 두 개의 십자가를 놓을 수 있는 경우만 입력으로 주어진다.
#
# 출력
# 첫째 줄에 놓은 십자가 넓이의 곱의 최댓값을 출력한다.
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def chk_range(y ,x):
    if 0 <= y < n and 0 <= x < m and grid[y][x] == '#':
        return True
    return False
def chk_cross(y, x):
    y1 = y2 = y3 = y4 = y
    x1 = x2 = x3 = x4 = x
    path = [(y, x)]
    res = [(len(path), path)]
    while True:
        y1, y2, y3, y4 = y1+dy[0], y2+dy[1], y3+dy[2], y4+dy[3]
        x1, x2, x3, x4 = x1+dx[0], x2+dx[1], x3+dx[2], x4+dx[3]
        if not (chk_range(y1, x1) and chk_range(y2, x2) and chk_range(y3, x3) and chk_range(y4, x4)):
            break
        path.append((y1, x1))
        path.append((y2, x2))
        path.append((y3, x3))
        path.append((y4, x4))
        tmp = path[:]
        res.append((len(tmp), tmp))
    return res
answer = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            answer.extend(chk_cross(i, j))
answer.sort(key=lambda x: x[0], reverse=True)
ans = 0
for i in range(len(answer)-1):
    for j in range(i+1, len(answer)):
        if set(answer[i][1]) & set(answer[j][1]):
            continue
        else:
            ans = max(ans, answer[i][0]*answer[j][0])
            break
print(ans)
