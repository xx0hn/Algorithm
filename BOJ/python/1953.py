# 문제
# 2007년 1월 9일(화)는 원장선생님의 말씀대로 어제와 같이 하루 일과를 팀플레이를 통해 하려고 한다. 이 날은 특별히 청팀과 백팀으로 두 팀을 나누어 팀전을 하려 한다. 하지만 어제 하루 팀플레이를 하면서, 서로 같은 팀을 하기 싫어하는 사람들이 생겼다.
#
# 이제 우리가 할 일은 다음과 같다. 사람들이 각각 싫어하는 사람들의 정보가 주어져 있을 때, 그 사람들의 요구를 수용하여 서로 싫어하는 사람은 같은 팀에 넣지 않으려 한다. 이 조건을 만족하여 n명의 사람들 두 팀으로 나누는 프로그램을 작성하여라.
#
# 입력
# 첫 줄에는 학생들의 수 n (1 ≤ n ≤ 100)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 서로가 싫어하는 사람들의 정보가 주어진다. i+1번째 줄에는 i번째 사람이 싫어하는 사람의 수와 싫어하는 사람들이 나온다.
#
# 모든 사람이 싫어하는 사람이 단 한 명도 없는 경우는 없다.
#
# 출력
# 첫줄에는 청팀의 사람의 수를 출력하고, 그리고 둘째 줄에는 청팀에 속한 사람들을 오름차순으로 나열한다. 그리고 셋째 줄과 넷째 줄은 위와 같은 방법으로 백팀에 속한 인원의 수, 백팀에 속한 사람들을 출력한다. 단 답이 여러 가지 일 경우에는 한 가지만 출력하여도 좋다.
from collections import deque
n = int(input())
hater = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp)):
        hater[i][tmp[j]] = 1
        hater[tmp[j]][i] = 1
visited = [False for _ in range(n+1)]
result = [0 for _ in range(n+1)]
def bfs(cur, t):
    q = deque()
    q.append((cur, t))
    visited[cur] = True
    result[cur] = t
    while q:
        cur, tm = q.popleft()
        for nxt in range(1, n+1):
            if hater[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                result[nxt] = -tm
                q.append((nxt, -tm))
for num in range(1, n+1):
    if not visited[num]:
        bfs(num, 1)
team = [[] for _ in range(2)]
for i in range(1, n+1):
    if result[i] == -1:
        team[0].append(i)
    elif result[i] == 1:
        team[1].append(i)
for i in range(2):
    print(len(team[i]))
    print(*team[i])
