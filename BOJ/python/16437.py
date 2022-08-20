# 문제
# N개의 섬으로 이루어진 나라가 있습니다. 섬들은 1번 섬부터 N번 섬까지 있습니다.
#
# 1번 섬에는 구명보트만 있고 다른 섬에는 양들 또는 늑대들이 살고 있습니다.
#
# 늘어나는 늑대의 개체 수를 감당할 수 없던 양들은 구명보트를 타고 늑대가 없는 나라로 이주하기로 했습니다.
#
# 각 섬에서 1번 섬으로 가는 경로는 유일하며 i번 섬에는 pi번 섬으로 가는 다리가 있습니다.
#
# 양들은 1번 섬으로 가는 경로로 이동하며 늑대들은 원래 있는 섬에서 움직이지 않고 섬으로 들어온 양들을 잡아먹습니다. 늑대는 날렵하기 때문에 섬에 들어온 양을 항상 잡을 수 있습니다. 그리고 늑대 한 마리는 최대 한 마리의 양만 잡아먹습니다.
#
# 얼마나 많은 양이 1번 섬에 도달할 수 있을까요?
#
# 입력
# 첫 번째 줄에 섬의 개수 N (2 ≤ N ≤ 123,456) 이 주어집니다.
#
# 두 번째 줄부터 N-1개에 줄에 2번 섬부터 N번 섬까지 섬의 정보를 나타내는 ti, ai, pi (1 ≤ ai ≤ 109, 1 ≤ pi ≤ N) 가 주어집니다.
#
# ti가 'W' 인 경우 i번 섬에 늑대가 ai마리가 살고 있음을, ti가 'S'인 경우 i번 섬에 양이 ai마리가 살고 있음을 의미합니다. pi는 i번째 섬에서 pi번 섬으로 갈 수 있는 다리가 있음을 의미합니다.
#
# 출력
# 첫 번째 줄에 구출할 수 있는 양의 수를 출력합니다.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
bridges = [[] for _ in range(n+1)]
islands = [0 for _ in range(n+1)]
for i in range(2, n+1):
    t, a, p = map(str, input().split())
    bridges[int(p)].append(i)
    if t == 'S':
        islands[i] = int(a)
    else:
        islands[i] = -int(a)
visited = [False for _ in range(n+1)]
def move_sheep(node):
    s = islands[node]
    for nxt in bridges[node]:
        s += move_sheep(nxt)
    if s < 0:
        return 0
    else:
        return s
print(move_sheep(1))
