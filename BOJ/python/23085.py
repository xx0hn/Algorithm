# 문제
# 판치기는 \(N\)개의 동전을 바닥에 놓고, 임의의 동전들을 뒤집는 것을 반복하여 모두 뒷면이 보이는 상태로 바꾸면 이기는 게임이다.
#
# 판치기 경력 20년에 빛나는 치훈이는 판치기 최고의 극의, "\(K\)-뒤집기"를 시전할 수 있게 되었다. "\(K\)-뒤집기"는 원하는 서로 다른 \(K\)개의 동전을 한 번에 뒤집는 능력이다.
#
# 초기 동전의 상태가 주어진다. "\(K\)-뒤집기"만 사용해 게임을 이기려면 최소 몇 번 사용해야 이길 수 있을까?
#
# 입력
# 첫째 줄에 \(N\), \(K\)가 주어진다.
#
# 두번째 줄에 초기 동전의 상태를 나타내는 문자열 \(S\)가 주어진다.
#
#  \(S\)의 \(i\)번째 문자가 'H'면 \(i\)번째 동전이 앞면, 'T'면 \(i\)번째 동전이 뒷면이 보이는 상태를 나타낸다.
#
# 출력
# 첫째 줄에 문제의 답을 출력한다.
#
# 모두 뒷면이 보이는 상태로 바꿀 수 없다면 대신 -1을 출력한다.
#
# 제한
# 1 ≤ \(N\) ≤ 3,000
# 1 ≤ \(K\) ≤ \(N\) 
from collections import deque
n, k = map(int, input().split())
coins = list(str(input()))
front, back = 0, 0
for i in range(n):
    if coins[i] == 'H':
        front += 1
    else:
        back += 1
def find_answer():
    q = deque()
    q.append((back, 0))
    visited = [0 for _ in range(n+1)]
    visited[back] = True
    while q:
        bk, cnt = q.popleft()
        if bk == n:
            return cnt
        ft = n-bk
        for i in range(k+1):
            turn_b, turn_f = i, k-i
            if turn_b > bk or turn_f > ft:
                continue
            nxt_bk = bk-turn_b+turn_f
            if not visited[nxt_bk]:
                visited[nxt_bk] = True
                q.append((nxt_bk, cnt+1))
    return -1
print(find_answer())
