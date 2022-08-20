# 문제
# 정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.
#
# 사용할 수 있는 연산은 아래와 같다.
#
# s = s + s; (출력: +)
# s = s - s; (출력: -)
# s = s * s; (출력: *)
# s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)
# 입력
# 첫째 줄에 s와 t가 주어진다. (1 ≤ s, t ≤ 109)
#
# 출력
# 첫째 줄에 정수 s를 t로 바꾸는 방법을 출력한다. s와 t가 같은 경우에는 0을, 바꿀 수 없는 경우에는 -1을 출력한다. 가능한 방법이 여러 가지라면, 사전 순으로 앞서는 것을 출력한다.
#
# 연산의 아스키 코드 순서는 '*', '+', '-', '/' 이다.
from collections import deque
s, t = map(int, input().split())
def four_operations():
    q = deque()
    q.append((s, []))
    visited = set()
    visited.add(s)
    while q:
        cur, opers = q.popleft()
        if cur == t:
            return ''.join(opers)
        nxt = cur*cur
        if 0 <= nxt <= 10e9 and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, opers+['*']))
        nxt = cur+cur
        if 0 <= nxt <= 10e9 and nxt not in visited:
            visited.add(nxt)
            q.append((nxt, opers+['+']))
        if cur != 0:
            nxt = cur//cur
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, opers+['/']))
    return -1
answer = four_operations()
if not answer:
    answer = 0
print(answer)
