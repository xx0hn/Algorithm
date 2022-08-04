# 문제
# 영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.
#
# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.
#
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.
#
# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.
#
# 출력
# 첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.
from collections import deque
s = int(input())
def copy_to_clip(cur, clip):
    clip = cur
    return cur, clip
def add_to_cur(cur, clip):
    cur += clip
    return cur, clip
def delete_cur(cur, clip):
    cur -= 1
    return cur, clip
def bfs():
    q = deque()
    q.append((1, 0, 0))
    visited = [[False for _ in range(1001)] for _ in range(1001)]
    visited[1][0] = True
    while q:
        cur, clip, time = q.popleft()
        if cur > 1000 or cur < 0:
            continue
        if cur == s:
            return time
        nxt_cur, nxt_clip = copy_to_clip(cur, clip)
        if 0 <= nxt_cur <= 1000 and 0 <= nxt_clip <= 1000 and not visited[nxt_cur][nxt_clip]:
            visited[nxt_cur][nxt_clip] = True
            q.append((nxt_cur, nxt_clip, time+1))
        nxt_cur, nxt_clip = add_to_cur(cur, clip)
        if 0 <= nxt_cur <= 1000 and 0 <= nxt_clip <= 1000 and not visited[nxt_cur][nxt_clip]:
            visited[nxt_cur][nxt_clip] = True
            q.append((nxt_cur, nxt_clip, time+1))
        nxt_cur, nxt_clip = delete_cur(cur, clip)
        if 0 <= nxt_cur <= 1000 and 0 <= nxt_clip <= 1000 and not visited[nxt_cur][nxt_clip]:
            visited[nxt_cur][nxt_clip] = True
            q.append((nxt_cur, nxt_clip, time+1))
print(bfs())
