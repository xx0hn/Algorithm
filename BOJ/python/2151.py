# 문제
# 채영이는 거울을 들여다보는 것을 참 좋아한다. 그래서 집 곳곳에 거울을 설치해두고 집 안을 돌아다닐 때마다 거울을 보곤 한다.
#
# 채영이는 새 해를 맞이하여 이사를 하게 되었는데, 거울을 좋아하는 그녀의 성격 때문에 새 집에도 거울을 매달만한 위치가 여러 곳 있다. 또한 채영이네 새 집에는 문이 두 개 있는데, 채영이는 거울을 잘 설치하여 장난을 치고 싶어졌다. 즉, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 거울을 설치하고 싶어졌다.
#
# 채영이네 집에 대한 정보가 주어졌을 때, 한 쪽 문에서 다른 쪽 문을 볼 수 있도록 하기 위해 설치해야 하는 거울의 최소 개수를 구하는 프로그램을 작성하시오.
#
# 거울을 설치할 때에는 45도 기울어진 대각선 방향으로 설치해야 한다. 또한 모든 거울은 양면 거울이기 때문에 양 쪽 모두에서 반사가 일어날 수 있다. 채영이는 거울을 매우 많이 가지고 있어서 거울이 부족한 경우는 없다고 하자.
#
# 거울을 어떻게 설치해도 한 쪽 문에서 다른 쪽 문을 볼 수 없는 경우는 주어지지 않는다.
#
# 입력
# 첫째 줄에 집의 크기 N (2 ≤ N ≤ 50)이 주어진다. 다음 N개의 줄에는 N개의 문자로 집에 대한 정보가 주어진다. ‘#’는 문이 설치된 곳으로 항상 두 곳이며, ‘.’은 아무 것도 없는 것으로 빛은 이 곳을 통과한다. ‘!’은 거울을 설치할 수 있는 위치를 나타내고, ‘*’은 빛이 통과할 수 없는 벽을 나타낸다.
#
# 출력
# 첫째 줄에 설치해야 할 거울의 최소 개수를 출력한다.
import heapq
n = int(input())
grid = [list(str(input())) for _ in range(n)]
point = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            point.append((i, j))
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
def dijkstra():
    hq = []
    dists = [[[1e9 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    for i in range(4):
        heapq.heappush(hq, ((0, point[0][0], point[0][1], i)))
        dists[point[0][0]][point[0][1]][i] = 0
    while hq:
        mirror, y, x, d = heapq.heappop(hq)
        if mirror > dists[y][x][d]:
            continue
        if grid[y][x] == '!':
            for i in range(4):
                if i == (d+2)%4:
                    continue
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != '*':
                    if i != d:
                        if dists[ny][nx][i] >= mirror+1:
                            dists[ny][nx][i] = mirror+1
                            heapq.heappush(hq, (mirror+1, ny, nx, i))
                    elif i == d:
                        if dists[ny][nx][d] >= mirror:
                            dists[ny][nx][d] = mirror
                            heapq.heappush(hq, (mirror, ny, nx, d))
        else:
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != '*':
                if dists[ny][nx][d] >= mirror:
                    dists[ny][nx][d] = mirror
                    heapq.heappush(hq, (mirror, ny, nx, d))
    return dists
answer = dijkstra()
print(min(answer[point[1][0]][point[1][1]]))
