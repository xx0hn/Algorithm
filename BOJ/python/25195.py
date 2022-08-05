# 문제
#
#
#  $N$개의 정점과 $M$개의 간선으로 이루어진, 사이클이 없는 방향그래프(DAG)가 주어진다.
#
# 투어리스트 곰곰이는 종종 이 그래프 위에서 여행을 떠난다. 투어리스트 곰곰이의 여행은 1번 정점에서 출발해 간선을 따라서 이동한다. 그러다가 더 이상 간선을 따라서 이동할 수 없는 경우 투어리스트의 여행은 종료된다.
#
# 투어리스트 곰곰이의 열성 팬인 팬클럽 곰곰이는 투어리스트를 만나기 위해 그래프 위의 정점 일부에서 잠복하곤 한다. 팬클럽 곰곰이가 잠복한 정점 위에 투어리스트 곰곰이가 서 있게 되면 투어리스트 곰곰이와 팬클럽 곰곰이가 만나게 된다.
#
# 오늘도 투어리스트 곰곰이는 음악을 들으면서 여행을 떠나려고 한다. 그러다가 Twice의 노래인 "YES or YES" 에서 다음과 같은 가사를 듣게 된다.
#
# 조금 쉽게 말하자면
# 넌 뭘 골라도 날 만나게 될 거야
# Twice, YES or YES 가사 중 일부
# 투어리스트 곰곰이는 Twice의 노래 가사처럼, 뭘 골라도 팬클럽 곰곰이를 만나게 될 것인지 궁금해졌다.
#
# 투어리스트 곰곰이가 어떻게 이동하더라도 팬클럽 곰곰이를 만나게 된다면 "Yes" 를, 팬클럽 곰곰이를 만나지 않고 이동하는 방법이 존재한다면 "yes" 를 출력하자.
#
# 입력
# 첫째 줄에는 정점의 개수 $N$과 간선의 개수 $M$이 주어진다. ($1 \leq N, M \leq 100\,000$)
#
# 이후 $M$줄에 걸쳐서 간선의 정보를 나타내는 두 정수 $u$, $v$ 가 주어진다. 이는 정점 $u$ 에서 정점 $v$ 로 가는 간선이 있음을 의미한다. ($1 \leq u$, $v \leq N$, $u \ne v$)
#
# 이후 $M+2$번째 줄에는 팬클럽 곰곰이가 존재하는 정점의 개수 $S$ 가 주어진다. ($1 \leq S \leq N$)
#
# 이후 $M+3$번째 줄에는 팬클럽 곰곰이가 존재하는 정점의 번호 $s$ 가 차례대로 $S$개 만큼 주어진다. ($1 \le s \le N$)
#
# 주어진 그래프는 사이클이 없음이 보장된다. 또한 두 정점을 연결하는 간선은 최대 한 개이다.
#
# 팬클럽 곰곰이가 존재하는 정점의 번호는 중복해서 주어지지 않는다.
#
# 출력
# 문제에서 설명한 조건에 맞춰서 Yes 또는 yes 를 출력한다.
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
s = int(input())
gg = list(map(int, input().split()))
visited = [False for _ in range(n+1)]
def bfs():
    q = deque()
    q.append(1)
    if visited[1]:
        return 'Yes'
    visited[1] = True
    while q:
        node = q.popleft()
        if not graph[node]:
            return 'yes'
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return 'Yes'
for g in gg:
    visited[g] = True
print(bfs())
