# 문제
# 창영이의 퇴근길은 출근길과 조금 다르다. 창영이는 건강을 위해 따릉이를 빌려 타고 퇴근하는 습관을 기르고 있다.
#
# 창영이의 퇴근길은 N×N 크기의 격자로 표현된다. 창영이는 A1,1에서 출발하여 AN,N까지 이동할 계획이다. 창영이는 상하좌우 인접한 격자로 한 번에 한 칸씩 이동할 수 있다. 각 격자 Ar,c에는 자연수가 적혀 있는데, 이는 해당 지역의 높이를 뜻한다. 인접한 격자 사이의 높이 차이의 절댓값을 경사라고 하고, 경사가 클수록 경사가 가파르다고 하자.
#
# 따릉이는 가격에 따라 성능이 다르다. 비싼 따릉이는 경사가 가파르더라도 내리지 않고 타고 갈 수 있지만, 값싼 따릉이는 경사가 가파르면 힘들고 위험하기 때문에 내려서 이동해야 한다.
#
# 창영이는 최소한의 비용으로 따릉이를 빌려서, 따릉이에서 한 번도 내리지 않고 집에 도착하고 싶다. 그러기 위해선 창영이가 지날 수 있는 최대 경사의 최솟값을 알아야만 한다. 여러분들이 창영이를 도와주자.
#
# 입력
# 첫째 줄에 격자의 크기 N이 주어진다.
#
# 둘째 줄부터 N개의 줄에 걸쳐 각 격자의 높이 정보가 주어진다. 첫 번째로 주어지는 값이 A1,1이고, 마지막으로 주어지는 값이 AN,N이다.
#
# 출력
# A1,1에서 AN,N까지, 경로상의 최대 경사의 최솟값을 출력한다.
#
# 제한
# 1 ≤ N ≤ 1,000
# 1 ≤ Ar,c ≤ 1,000,000,000
import heapq
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
sy, sx = 0, 0
def find_way():
    q = []
    heapq.heappush(q, (0, sy, sx))
    costs = [[1e9 for _ in range(n)] for _ in range(n)]
    costs[sy][sx] = 0
    while q:
        cost, y, x = heapq.heappop(q)
        if cost > costs[y][x]:
            continue
        if (y, x) == (n-1, n-1):
            return cost
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                nxt_cost = max(abs(grid[ny][nx] - grid[y][x]), cost)
                if costs[ny][nx] > nxt_cost:
                    costs[ny][nx] = nxt_cost
                    heapq.heappush(q, (nxt_cost, ny, nx))
    return -1
print(find_way())
