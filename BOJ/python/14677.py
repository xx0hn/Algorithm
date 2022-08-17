# 문제
# 윤호는 병약하다. 그래서 약을 먹어야 하는데 약은 아침, 점심, 저녁 한 번씩 먹어야 한다. 윤호는 hyo123bin 님에게 총 N일치 약을 받아왔다. N일치 이므로 약은 총 3N포가 들어있다.
#
#
#
# 윤호는 완벽주의자다. 따라서 총 3N개의 약이 한 줄로 나열되어 있을 때, 중간에 끊지 않고 약을 먹고 싶다. 즉, 맨 앞의 약과 맨 뒤의 약만을 꺼내 먹고 싶다. 만약 위와 같은 규칙을 지키지 못할 경우 윤호는 답답해서 죽어버린다. 과연 3N개의 약을 다 먹을 수 있을까? 못 먹는다면 최대 몇 개까지 먹을 수 있을까?
#
# 입력
# 프로그램의 입력은 표준 입력으로 받는다. 입력의 첫 줄에는 약을 먹어야 하는 날짜인 N이 주어진다. (1 ≤ N ≤ 500) 두 번째 줄에는 3N개의 약의 상태가 주어지는데, 아침 약은 B, 점심 약은 L, 저녁 약은 D로 주어진다. 약은 아침부터 먹기 시작한다.
#
# 출력
# 프로그램의 출력은 표준 출력으로 한다. 윤호가 먹을 수 있는 약의 최대 개수를 출력한다.
from collections import deque
n = int(input())
s = list(str(input()))
nxt = {'B': 'L', 'L': 'D', 'D': 'B'}
def find_max():
    q = deque()
    q.append((0, n*3-1, 'D', 0))
    result = 0
    visited = [[False for _ in range(n*3+1)] for _ in range(n*3+1)]
    visited[0][n*3-1] = True
    while q:
        l, r, cur, cnt = q.popleft()
        result = max(result, cnt)
        if l > r:
            return result
        for i in [l, r]:
            if s[i] == nxt[cur]:
                if i == l and not visited[i+1][r]:
                    visited[i+1][r] = True
                    q.append((i+1, r, nxt[cur], cnt+1))
                elif i == r and not visited[l][i-1]:
                    visited[l][i-1] = True
                    q.append((l, i-1, nxt[cur], cnt+1))
    return result
print(find_max())
