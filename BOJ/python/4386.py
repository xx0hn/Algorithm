# 문제
# 도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
#
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
#
# 입력
# 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
#
# 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.
#
# 출력
# 첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.
import math
import heapq
n = int(input())
star = [tuple(map(float, input().split())) for _ in range(n)]
def get_dist(a, b):
    y1, x1 = a
    y2, x2 = b
    return round(math.sqrt((y1-y2)**2 + (x1-x2)**2), 2)
def prim(start, weight):
    visited = [False for _ in range(n)]
    q = [(weight, start)]
    answer = 0
    cnt = 0
    while cnt < n:
        w, cur = heapq.heappop(q)
        if visited[cur]:
            continue
        visited[cur] = True
        answer += w
        cnt += 1
        for nxt, nxt_w in link[cur]:
            if visited[nxt]:
                continue
            heapq.heappush(q, (nxt_w, nxt))
    return answer
link = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist = get_dist(star[i], star[j])
        link[i].append((j, dist))
print(prim(0, 0))
