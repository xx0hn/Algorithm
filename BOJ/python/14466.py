# 문제
# 소가 길을 건너간 이유는 그냥 길이 많아서이다. 존의 농장에는 길이 너무 많아서, 길을 건너지 않고서는 별로 돌아다닐 수가 없다.
#
# 존의 농장에 대대적인 개편이 있었다. 이제 작은 정사각형 목초지가 N×N (2 ≤ N ≤ 100) 격자로 이루어져 있다. 인접한 목초지 사이는 일반적으로 자유롭게 건너갈 수 있지만, 그 중 일부는 길을 건너야 한다. 농장의 바깥에는 높은 울타리가 있어서 소가 농장 밖으로 나갈 일은 없다.
#
# K마리의 (1 ≤ K ≤ 100,K ≤ N2) 소가 존의 농장에 있고, 각 소는 서로 다른 목초지에 있다. 어떤 두 소는 길을 건너지 않으면 만나지 못 할 수 있다. 이런 소가 몇 쌍인지 세어보자.
#
# 입력
# 첫 줄에 N, K, R이 주어진다. 다음 R줄에는 한 줄에 하나씩 길이 주어진다. 길은 상하좌우로 인접한 두 목초지를 잇고, r c r′ c′의 형태 (행, 열, 행, 열)로 주어진다. 각 수는 1 이상 N 이하이다. 그 다음 K줄에는 한 줄의 하나씩 소의 위치가 행과 열로 주어진다.
#
# 출력
# 길을 건너지 않으면 만날 수 없는 소가 몇 쌍인지 출력한다.
from collections import deque
n, k, r = map(int, input().split())
road = [[[] for _ in range(n+1)] for _ in range(n+1)]
cow_map = [[False for _ in range(n+1)] for _ in range(n+1)]
cow_list = []
for i in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road[r1][c1].append([r2, c2])
    road[r2][c2].append([r1, c1])
for i in range(k):
    y, x = map(int, input().split())
    cow_list.append([y, x])
    cow_map[y][x] = True
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = 0
def find_cow(y, x):
    global k, result
    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    q = deque()
    q.append([y, x])
    cow_map[y][x] = False
    cnt = 0
    k -= 1
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 1 <= ny <= n and 1 <= nx <= n and not visited[ny][nx]:
                if [ny, nx] not in road[cy][cx]:
                    q.append([ny, nx])
                    visited[ny][nx] = True
                    if cow_map[ny][nx]:
                        cnt += 1
    result += k - cnt
for y, x in cow_list:
    if cow_map[y][x]:
        find_cow(y, x)
print(result)
