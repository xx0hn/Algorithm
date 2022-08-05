# 문제
# 여행을 마치고 꽉꽉나라로 돌아가던 중 오리와 육리는 서로를 잃어버렸다. 현재 오리는 점 A에 있고, 육리는 점 B에 있다.
#
# 오리와 육리는 서로를 찾기 위해 무조건 하루에 한 번씩 점프를 한다. 1일차에는 1만큼 점프하고 하루가 지날 때마다 서로가 더욱 보고 싶은 나머지 두 배씩 더 멀리 점프한다. 즉, 현재 위치가 X이고 서로를 찾기 시작한 지 y일차라면 점 X + 2y-1 또는 점 X - 2y-1로 점프한다. 0 이하의 점들과 N+1 이상의 점들은 디딜 땅이 없기 때문에 그곳으로 점프한다면 오리와 육리는 영원히 만나지 못한다.
#
# 아래 그림은 N = 10, A = 4, B = 10일 때의 예시이다. 화살표는 점프 가능한 위치를 나타낸다.
#
#
#
# 오리와 육리의 위치가 주어졌을 때, 둘이 만날 수 있는 최소 일수를 구해보자. 같은 날 같은 점의 땅에 도착했을 때 오리와 육리가 만난 것으로 간주한다.
#
# 입력
# 첫 번째 줄에 세 정수 N, A, B가 주어진다. (2 ≤ N ≤ 500,000, 1 ≤ A, B ≤ N, A ≠ B)
#
# 출력
# 첫 번째 줄에 오리와 육리가 만날 수 있는 최소 일수를 출력한다. 만약 오리와 육리가 영원히 만날 수 없다면 -1을 출력한다.
from collections import deque
n, a, b = map(int, input().split())
d = [1, -1]
a_visited = [[-1 for _ in range(20)] for _ in range(n+1)]
b_visited = [[-1 for _ in range(20)] for _ in range(n+1)]
def bfs_a(a):
    q = deque()
    q.append((a, 0))
    a_visited[a][0] = 0
    while q:
        cur, day = q.popleft()
        for i in range(2):
            nxt = cur+d[i]*(2**day)
            if 1 <= nxt <= n and a_visited[nxt][day+1] == -1:
                a_visited[nxt][day+1] = day+1
                q.append((nxt, day+1))
def bfs_b(b):
    q = deque()
    q.append((b, 0))
    b_visited[b][0] = 0
    while q:
        cur, day = q.popleft()
        if a_visited[cur][day] == b_visited[cur][day]:
            return day
        for i in range(2):
            nxt = cur+d[i]*(2**day)
            if 1 <= nxt <= n and b_visited[nxt][day+1] == -1:
                b_visited[nxt][day+1] = day+1
                q.append((nxt, day+1))
    return -1
bfs_a(a)
print(bfs_b(b))
