# 문제
# 아주 먼 미래에 사람들이 가장 많이 사용하는 대중교통은 하이퍼튜브이다. 하이퍼튜브 하나는 역 K개를 서로 연결한다. 1번역에서 N번역으로 가는데 방문하는 최소 역의 수는 몇 개일까?
#
# 입력
# 첫째 줄에 역의 수 N과 한 하이퍼튜브가 서로 연결하는 역의 개수 K, 하이퍼튜브의 개수 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ K, M ≤ 1000)
#
# 다음 M개 줄에는 하이퍼튜브의 정보가 한 줄에 하나씩 주어진다. 총 K개 숫자가 주어지며, 이 숫자는 그 하이퍼튜브가 서로 연결하는 역의 번호이다.
#
# 출력
# 첫째 줄에 1번역에서 N번역으로 가는데 방문하는 역의 개수의 최솟값을 출력한다. 만약, 갈 수 없다면 -1을 출력한다.
from collections import deque
n, k, m = map(int, input().split())
station = [[] for _ in range(n+1)]
tube = [[] for _ in range(m)]
for i in range(m):
    nums = list(map(int, input().split()))
    for num in nums:
        station[num].append(i)
        tube[i].append(num)
def find_way():
    q = deque()
    q.append((1, 1))
    visited_station = [False for _ in range(n+1)]
    visited_tube = [False for _ in range(m)]
    visited_station[1] = True
    while q:
        cur, cnt = q.popleft()
        if cur == n:
            return cnt
        nxt_tube = []
        for nxt in station[cur]:
            if not visited_tube[nxt]:
                nxt_tube.append(nxt)
                visited_tube[nxt] = True
        for nxt in nxt_tube:
            for idx in tube[nxt]:
                if not visited_station[idx]:
                    visited_station[idx] = True
                    q.append((idx, cnt+1))
    return -1
print(find_way())
