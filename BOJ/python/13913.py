# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
#
# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
#
# 둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
from collections import deque
n, k=map(int, input().split())
dw=[1, -1, 0]
dt=[1, 1, 2]
def bfs():
    visited=[False for _ in range(2*(k-1)+1)]
    visited[n]=True
    q=deque()
    q.append((0, n, [n]))
    while q:
        time, cur, path=q.popleft()
        if cur==k:
            return [time, path]
        for i in range(3):
            nxt=(cur+dw[i])*dt[i]
            if 0<=nxt<=2*(k-1) and not visited[nxt]:
                visited[nxt]=True
                q.append((time+1, nxt, path+[nxt]))
if n>k:
    print(n-k)
    print(*list(range(n, k-1, -1)))
elif n==0 and k==1:
    print(k-n)
    print(*[n, k])
else:
    answer=bfs()
    print(answer[0])
    print(*answer[1])
