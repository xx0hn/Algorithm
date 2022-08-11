# 문제
# 우주 탐사선 ana호는 어떤 행성계를 탐사하기 위해 발사된다. 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하려 한다. 입력으로는 ana호가 탐색할 행성의 개수와 ana호가 발사되는 행성의 위치와 ana호가 행성 간 이동을 하는데 걸리는 시간이 2차원 행렬로 주어진다. 행성의 위치는 0부터 시작하여 0은 행렬에서 0번째 인덱스에 해당하는 행성을 의미한다. 2차원 행렬에서 i, j 번 요소는 i 번째 행성에서 j 번째 행성에 도달하는데 걸리는 시간을 나타낸다. i와 j가 같을 때는 항상 0이 주어진다. 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하여라.
#
# 탐사 후 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.
#
# 입력
# 첫 번째 줄에는 행성의 개수 N과 ana호가 발사되는 행성의 위치 K가 주어진다. (2 ≤ N ≤ 10, 0 ≤ K < N)
#
# 다음 N 줄에 걸쳐 각 행성 간 이동 시간 Tij 가 N 개 씩 띄어쓰기로 구분되어 주어진다. (0 ≤ Tij  ≤ 1000)
#
# 출력
# 모든 행성을 탐사하기 위한 최소 시간을 출력한다.
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = 1e9
for d in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][d]+graph[d][j])
def find_min(cur, time, chk):
    global answer
    if chk == n:
        answer = min(answer, time)
        return
    for nxt in range(n):
        if not visited[nxt]:
            visited[nxt] = True
            find_min(nxt, time+graph[cur][nxt], chk+1)
            visited[nxt] = False
visited[k] = True
find_min(k, 0, 1)
print(answer)
