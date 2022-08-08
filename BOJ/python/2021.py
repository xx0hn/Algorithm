# 문제
# 어떤 도시의 지하철 노선에 대한 정보가 주어졌을 때, 출발지에서 목적지까지의 최소 환승 경로를 구하는 프로그램을 작성하시오. 실제 경로를 구할 필요는 없고, 환승 회수만을 구하면 된다.
#
# 입력
# 첫째 줄에 역의 개수 N(1≤N≤100,000), 노선의 개수 L(1≤L≤100,000)이 주어진다. 다음 L개의 줄에는 각 노선이 지나는 역이 순서대로 주어지며 각 줄의 마지막에는 -1이 주어진다. 마지막 줄에는 출발지 역의 번호와 목적지 역의 번호가 주어진다. 역 번호는 1부터 N까지의 정수로 표현된다. 각 노선의 길이의 합은 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 최소 환승 회수를 출력한다. 불가능한 경우에는 -1을 출력한다.
from collections import deque
n, l = map(int, input().split())
stations = [[] for _ in range(n+1)]
lines = []
for i in range(l):
    tmp = list(map(int, input().split()))
    lines.append(tmp[:-1])
    for j in range(len(tmp)-1):
        stations[tmp[j]].append(i)
start, end = map(int, input().split())
def bfs():
    if start == end:
        return 0
    visited = [-1 for _ in range(n+1)]
    visited_line = [False for _ in range(l)]
    q = deque()
    for line in stations[start]:
        q.append((start, line))
        visited_line[line] = True
    visited[start] = 0
    if start == end:
        return 0
    while q:
        cur, cur_l = q.popleft()
        if cur == end:
            return visited[cur]-1
        for nxt in lines[cur_l]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur]+1
                for nxt_l in stations[nxt]:
                    if not visited_line[nxt_l]:
                        q.append((nxt, nxt_l))
    return -1
print(bfs())
