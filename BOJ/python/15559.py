# 문제
# 욱제는 구사과의 열렬한 팬이다. 오늘 욱제는 구사과에게 선물()을 전달해주려고 한다. 지난 며칠간의 관찰 끝에 욱제는 구사과의 이동 패턴을 모두 파악했다.
#
# 구사과가 있는 곳은 N×M 크기의 직사각형 지도로 나타낼 수 있으며, 1×1크기의 정사각형으로 나누어져 있다. 구사과의 위치는 (i, j)로 나타낼 수 있으며, (i, j)는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸을 의미한다.
#
# 지도의 각 칸에는 N, W, E, S 중의 한 문자가 쓰여져 있는데, 구사과는 이 문자를 이용해서 이동한다. 구사과의 위치가 (i, j)인 경우에 N이 쓰여져 있는 칸에 서 있었다면, (i-1, j)로, S의 경우에는 (i+1, j)로, W의 경우에는 (i, j-1), E의 경우에는 (i, j+1)로 순간이동한다. 구사과는 지치지 않기 때문에, 계속해서 이동한다.
#
# 욱제는 구사과의 위치를 모르기 때문에, 구사과가 이동을 시작하는 위치와 관계없이 선물을 주는 방법을 알아내려고 한다. 최소 몇 개의 칸 위에 선물을 놓으면, 구사과가 항상 선물을 가져가는지 구하는 프로그램을 작성하시오. 선물이 놓여진 칸에 구사과가 이동하면, 구사과는 항상 선물을 가져간다.
#
# 입력
# 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000, 1 < N×M ≤ 1,000,000)
#
# 둘째 줄부터 N개의 줄에는 구사과가 있는 곳의 지도가 주어진다.
#
# 지도에 쓰여 있는대로 이동했을 때, 지도를 벗어나는 경우는 없다.
#
# 출력
# 첫째 줄에 최소 몇 개의 칸에 선물을 놓아야 하는지 출력한다.
n, m = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
mapping = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
answer = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
def dfs(sy, sx, cnt):
    if visited[sy][sx]:
        return visited[sy][sx]
    visited[sy][sx] = cnt
    d = mapping[grid[sy][sx]]
    ny, nx = sy+dy[d], sx+dx[d]
    visited[sy][sx] = dfs(ny, nx, cnt)
    return visited[sy][sx]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            tmp = dfs(i, j, answer+1)
            answer = max(answer, tmp)
print(answer)
