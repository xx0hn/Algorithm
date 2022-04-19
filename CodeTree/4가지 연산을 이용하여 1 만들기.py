# 4가지 연산을 이용하여 1 만들기
# 숫자 N이 주어졌을 때, 다음 4가지 연산을 적절히 사용하여 연산의 횟수를 최소화 하여 숫자 1을 만들어 내려고 합니다.

# 현재 숫자에서 1을 뺍니다.

# 현재 숫자에 1을 더합니다.

# 현재 숫자가 2로 나누어 떨어질 경우, 현재 숫자를 2로 나눕니다.

# 현재 숫자가 3으로 나누어 떨어질 경우, 현재 숫자를 3으로 나눕니다.

# 예를 들어 숫자 11에서 시작하여 숫자 1을 만들어 내기 위해서는 최소 4번의 연산이 필요합니다.



# 1을 만들기 위해 필요한 최소 연산 횟수를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 숫자 N이 주어집니다.

# 1 ≤ N ≤ 1,000,000
# 출력 형식
# 숫자 N을 1로 만드는 데 필요한 최소 연산 횟수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 11
# 출력:

# 4
# 예제2
# 입력:

# 15
# 출력:

# 4
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
n=int(input())
cul=[1, -1]
visited=[-1 for _ in range(n*2+1)]
def bfs():
    global answer
    q=deque()
    q.append(n)
    visited[n]=0
    while q:
        cur=q.popleft()
        if cur%2==0:
            nxt=cur//2
            if 0<nxt<=n*2 and (visited[nxt]==-1 or visited[nxt]>visited[cur]+1):
                visited[nxt]=visited[cur]+1
                q.append(nxt)
        if cur%3==0:
            nxt=cur//3
            if 0<nxt<=n*2 and (visited[nxt]==-1 or visited[nxt]>visited[cur]+1):
                visited[nxt]=visited[cur]+1
                q.append(nxt)
        for i in range(2):
            nxt=cur+cul[i]
            if 0<nxt<=n*2 and (visited[nxt]==-1 or visited[nxt]>visited[cur]+1):
                visited[nxt]=visited[cur]+1
                q.append(nxt)
bfs()
answer=visited[1]
print(answer)
