# 문제
# N(2≤N≤1,000)개의 노드로 이루어진 트리가 주어지고 M(M≤1,000)개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.
#
# 입력
# 첫째 줄에 노드의 개수 N이 입력되고 다음 N-1개의 줄에 트리 상에 연결된 두 점과 거리(10,000 이하의 정수)를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 M개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.
#
# 출력
# M개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.
from collections import deque
def bfs(start, end):
    visited = [-1] * (n + 1)
    visited[start]=0
    q=deque()
    q.append(start)
    while q:
        cur=q.popleft()
        if cur==end:
            break
        for next, dist in tree[cur]:
            if visited[next]>-1:
                continue
            visited[next]=visited[cur]+dist
            q.append(next)
    return visited[end]
n, m=map(int ,input().split())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d=map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))
for _ in range(m):
    s, e=map(int, input().split())
    print(bfs(s, e))
